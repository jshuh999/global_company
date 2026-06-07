from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import redirect, render
from django.urls import reverse

from .table_registry import TABLES, get_table


PAGE_SIZE = 20


def quote_ident(identifier):
    return '"' + identifier.replace('"', '""') + '"'


def table_name(config):
    return f"{quote_ident(config.schema)}.{quote_ident(config.table)}"


def select_list(config):
    return ", ".join(quote_ident(field.name) for field in config.fields)


def where_clause(config):
    return " AND ".join(f"{quote_ident(field)} = %s" for field in config.pk_fields)


def pk_values_from_path(config, pk_path):
    values = pk_path.split("/") if pk_path else []
    if len(values) != len(config.pk_fields):
        raise ValueError("Invalid primary key path.")
    return values


def pk_path(config, row):
    return "/".join(str(row[field]) for field in config.pk_fields)


def normalize_for_input(value):
    if value is None:
        return ""
    if hasattr(value, "strftime"):
        if hasattr(value, "hour"):
            return value.strftime("%Y-%m-%dT%H:%M:%S")
        return value.strftime("%Y-%m-%d")
    return str(value)


def coerce_value(field, raw_value):
    if raw_value == "":
        return None
    if field.data_type == "number":
        try:
            value = Decimal(raw_value)
        except InvalidOperation as exc:
            raise ValueError(f"{field.label} 값이 숫자가 아닙니다.") from exc
        if field.scale == 0:
            return int(value)
        return value
    return raw_value


def form_values(config, post_data=None, row=None):
    values = {}
    errors = []
    for field in config.fields:
        if post_data is None:
            values[field.name] = normalize_for_input(row.get(field.name)) if row else ""
            continue
        raw_value = post_data.get(field.name, "").strip()
        if field.required and raw_value == "":
            errors.append(f"{field.label}은(는) 필수입니다.")
        try:
            values[field.name] = coerce_value(field, raw_value)
        except ValueError as exc:
            errors.append(str(exc))
            values[field.name] = raw_value
    return values, errors


def fetch_rows(config, page_number):
    order_by = ", ".join(quote_ident(field) for field in config.pk_fields)
    sql = f"SELECT {select_list(config)} FROM {table_name(config)} ORDER BY {order_by}"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    paginator = Paginator(rows, PAGE_SIZE)
    return paginator.get_page(page_number)


def fetch_row(config, pk_path_value):
    sql = f"SELECT {select_list(config)} FROM {table_name(config)} WHERE {where_clause(config)}"
    with connection.cursor() as cursor:
        cursor.execute(sql, pk_values_from_path(config, pk_path_value))
        row = cursor.fetchone()
        if row is None:
            return None
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, row))


def insert_row(config, values):
    fields = [field.name for field in config.fields]
    columns = ", ".join(quote_ident(field) for field in fields)
    placeholders = ", ".join(["%s"] * len(fields))
    sql = f"INSERT INTO {table_name(config)} ({columns}) VALUES ({placeholders})"
    with connection.cursor() as cursor:
        cursor.execute(sql, [values[field] for field in fields])


def update_row(config, values, pk_path_value):
    fields = [field.name for field in config.non_pk_fields]
    assignments = ", ".join(f"{quote_ident(field)} = %s" for field in fields)
    sql = f"UPDATE {table_name(config)} SET {assignments} WHERE {where_clause(config)}"
    params = [values[field] for field in fields] + pk_values_from_path(config, pk_path_value)
    with connection.cursor() as cursor:
        cursor.execute(sql, params)


def delete_row(config, pk_path_value):
    sql = f"DELETE FROM {table_name(config)} WHERE {where_clause(config)}"
    with connection.cursor() as cursor:
        cursor.execute(sql, pk_values_from_path(config, pk_path_value))


def table_index(request):
    return render(request, "common/table_index.html", {"tables": TABLES.values()})


def table_list(request, table_key):
    config = get_table(table_key)
    page_obj = fetch_rows(config, request.GET.get("page"))
    return render(
        request,
        "common/table_list.html",
        {"config": config, "fields": config.fields, "page_obj": page_obj},
    )


def table_create(request, table_key):
    config = get_table(table_key)
    if config.readonly:
        messages.warning(request, "조회 전용 테이블입니다.")
        return redirect("common:table-list", table_key=table_key)
    values, errors = form_values(config)
    if request.method == "POST":
        values, errors = form_values(config, request.POST)
        if not errors:
            insert_row(config, values)
            messages.success(request, "등록했습니다.")
            return redirect("common:table-list", table_key=table_key)
    return render(request, "common/table_form.html", {"config": config, "fields": config.fields, "values": values, "errors": errors, "mode": "create"})


def table_update(request, table_key, pk_path_value):
    config = get_table(table_key)
    if config.readonly:
        messages.warning(request, "조회 전용 테이블입니다.")
        return redirect("common:table-list", table_key=table_key)
    row = fetch_row(config, pk_path_value)
    if row is None:
        messages.error(request, "대상 데이터를 찾지 못했습니다.")
        return redirect("common:table-list", table_key=table_key)
    values, errors = form_values(config, row=row)
    if request.method == "POST":
        values, errors = form_values(config, request.POST)
        if not errors:
            update_row(config, values, pk_path_value)
            messages.success(request, "수정했습니다.")
            return redirect("common:table-list", table_key=table_key)
    return render(request, "common/table_form.html", {"config": config, "fields": config.fields, "values": values, "errors": errors, "mode": "update"})


def table_delete(request, table_key, pk_path_value):
    config = get_table(table_key)
    if config.readonly:
        messages.warning(request, "조회 전용 테이블입니다.")
        return redirect("common:table-list", table_key=table_key)
    row = fetch_row(config, pk_path_value)
    if row is None:
        messages.error(request, "대상 데이터를 찾지 못했습니다.")
        return redirect("common:table-list", table_key=table_key)
    if request.method == "POST":
        delete_row(config, pk_path_value)
        messages.success(request, "삭제했습니다.")
        return redirect("common:table-list", table_key=table_key)
    return render(request, "common/table_confirm_delete.html", {"config": config, "fields": config.fields, "row": row})


def table_detail(request, table_key, pk_path_value):
    config = get_table(table_key)
    row = fetch_row(config, pk_path_value)
    if row is None:
        messages.error(request, "대상 데이터를 찾지 못했습니다.")
        return redirect("common:table-list", table_key=table_key)
    update_url = reverse("common:table-update", kwargs={"table_key": table_key, "pk_path_value": pk_path_value})
    delete_url = reverse("common:table-delete", kwargs={"table_key": table_key, "pk_path_value": pk_path_value})
    return render(request, "common/table_detail.html", {"config": config, "fields": config.fields, "row": row, "update_url": update_url, "delete_url": delete_url})
