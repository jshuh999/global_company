-- lineage verification SQL samples
SELECT c."CUST_ID", c."CUST_NM", c."EADDR", c."PHONE_NO"
FROM global_company."CUSTOMER" c
WHERE c."CUST_ID" = :cust_id;

SELECT ca."CUST_ID", ca."ADDR_NM", ca."ZIP_CD", ca."RSLT_ADDR1", ca."RSLT_ADDR2"
FROM global_company."CUSTOMER_ADDR" ca
WHERE ca."CUST_ID" = :cust_id;

SELECT p."PROD_CD", p."PROD_NM", p."PROD_DVSN_CD", p."NTSL_PRC", p."STOCK_QTY"
FROM global_company."PRODUCT" p
WHERE p."PROD_CD" = :prod_cd;

SELECT oi."ORD_NO", oi."PROD_ORD", oi."PROD_CD", oi."QTY", oi."UNPRC", oi."AMT"
FROM global_company."ORDER_ITEM" oi
WHERE oi."ORD_NO" = :ord_no;
