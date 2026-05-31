from django.db import connection


def fetch_customer_contact(cust_no: str):
    sql = """
    SELECT cc.cust_no, cc.contact_value
    FROM global_company.customer_contacts cc
    WHERE cc.cust_no = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [cust_no])
        return cursor.fetchall()


def fetch_order_amount(order_no: str):
    sql = """
    SELECT so.order_no, so.order_amount, so.cust_no
    FROM global_company.sales_orders so
    WHERE so.order_no = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [order_no])
        return cursor.fetchall()
