-- lineage verification SQL samples
SELECT c.cst_id, c.cst_nm, c.eaddr, c.telno
FROM global_company.customer c
WHERE c.cst_id = :cst_id;

SELECT ca.cst_id, ca.addr_nm, ca.zipno, ca.rslt_addr, ca.rslt_addr2
FROM global_company.customer_addr ca
WHERE ca.cst_id = :cst_id;

SELECT p.prod_cd, p.prod_nm, p.prod_dvsn_cd, p.ntsl_prc, p.stock_qty
FROM global_company.product p
WHERE p.prod_cd = :prod_cd;

SELECT oi.ord_no, oi.prod_ord, oi.prod_cd, oi.qty, oi.unprc, oi.amt
FROM global_company.order_item oi
WHERE oi.ord_no = :ord_no;
