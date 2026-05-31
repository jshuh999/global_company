-- lineage verification SQL samples
SELECT c.cust_no, c.customer_name, cc.contact_value
FROM global_company.customers c
JOIN global_company.customer_contacts cc ON cc.customer_id = c.customer_id
WHERE c.cust_no = :cust_no;

SELECT p.product_code, p.product_name, i.stock_quantity
FROM global_company.products p
JOIN global_company.product_inventory i ON i.product_id = p.product_id
WHERE p.product_code = :product_code;

SELECT so.order_no, so.cust_no, soi.product_code, soi.order_item_amount
FROM global_company.sales_orders so
JOIN global_company.sales_order_items soi ON soi.order_id = so.order_id
WHERE so.order_no = :order_no;

SELECT v.voucher_no, a.account_subject_code, vl.line_amount
FROM global_company.vouchers v
JOIN global_company.voucher_lines vl ON vl.voucher_id = v.voucher_id
JOIN global_company.account_subjects a ON a.account_subject_id = vl.account_subject_id
WHERE v.voucher_no = :voucher_no;
