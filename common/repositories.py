from django.db import connection


def fetch_customer_contact(cust_no: str):
    sql = """
    SELECT c."CUST_ID", c."CUST_NM", c."EADDR", c."PHONE_NO"
    FROM global_company."CUSTOMER" c
    WHERE c."CUST_ID" = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [cust_no])
        return cursor.fetchall()


def fetch_order_items(order_no: str):
    sql = """
    SELECT oi."ORD_NO", oi."PROD_ORD", oi."PROD_CD", oi."QTY", oi."UNPRC", oi."AMT"
    FROM global_company."ORDER_ITEM" oi
    WHERE oi."ORD_NO" = %s
    ORDER BY oi."PROD_ORD"
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [order_no])
        return cursor.fetchall()
