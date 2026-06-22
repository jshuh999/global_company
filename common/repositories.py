from django.db import connection


def fetch_customer_contact(cust_no: str):
    sql = """
    SELECT c.cst_id, c.cst_nm, c.eaddr, c.telno
    FROM global_company.customer c
    WHERE c.cst_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [cust_no])
        return cursor.fetchall()


def fetch_order_items(order_no: str):
    sql = """
    SELECT oi.ord_no, oi.prod_ord, oi.prod_cd, oi.qty, oi.unprc, oi.amt
    FROM global_company.order_item oi
    WHERE oi.ord_no = %s
    ORDER BY oi.prod_ord
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [order_no])
        return cursor.fetchall()
