from dataclasses import dataclass
from typing import Optional

from django.http import Http404


@dataclass(frozen=True)
class FieldConfig:
    name: str
    label: str
    data_type: str
    required: bool = False
    scale: Optional[int] = None
    max_length: Optional[int] = None


@dataclass(frozen=True)
class TableConfig:
    key: str
    label: str
    schema: str
    table: str
    pk_fields: tuple[str, ...]
    fields: tuple[FieldConfig, ...]
    readonly: bool = False

    @property
    def non_pk_fields(self):
        return tuple(field for field in self.fields if field.name not in self.pk_fields)


TABLES = {
    "customer": TableConfig(
        key="customer",
        label="고객",
        schema="global_company",
        table="CUSTOMER",
        pk_fields=("CUST_ID",),
        fields=(
            FieldConfig("CUST_NM", "고객명", "text", True, max_length=50),
            FieldConfig("CUST_ID", "고객ID", "text", True, max_length=20),
            FieldConfig("EADDR", "이메일주소", "text", max_length=200),
            FieldConfig("PHONE_NO", "전화번호", "text", max_length=20),
            FieldConfig("BIRTH_DT", "생년월일", "date"),
            FieldConfig("GRADE_CD", "등급코드", "text", max_length=2),
            FieldConfig("CST_ADDR", "고객주소", "text", max_length=1000),
            FieldConfig("JOIN_DTTM", "가입일시", "datetime"),
            FieldConfig("LAST_LGN_DTTM", "최종로그인일시", "datetime"),
            FieldConfig("USE_YN", "사용여부", "text", True, max_length=1),
            FieldConfig("REG_DTM", "등록일시", "datetime", True),
            FieldConfig("REG_DT", "등록일자", "date", True),
        ),
    ),
    "customer-addr": TableConfig(
        key="customer-addr",
        label="고객주소",
        schema="global_company",
        table="CUSTOMER_ADDR",
        pk_fields=("CUST_ID", "CST_ADDR"),
        fields=(
            FieldConfig("CUST_ID", "고객ID", "text", True, max_length=20),
            FieldConfig("CST_ADDR", "고객주소", "text", True, max_length=1000),
            FieldConfig("ADDR_NM", "주소명", "text", True, max_length=100),
            FieldConfig("ZIP_CD", "우편번호", "text", max_length=6),
            FieldConfig("RSLT_ADDR1", "결과주소1", "text", max_length=300),
            FieldConfig("RSLT_ADDR2", "결과주소2", "text", max_length=300),
            FieldConfig("USE_YN", "사용여부", "text", True, max_length=1),
            FieldConfig("REG_DTM", "등록일시", "datetime", True),
            FieldConfig("RGTR_NM", "등록자명", "text", True, max_length=500),
        ),
    ),
    "customer-log": TableConfig(
        key="customer-log",
        label="고객변경로그",
        schema="global_company",
        table="CUSTOMER_LOG",
        pk_fields=("LOG_DTTM",),
        readonly=True,
        fields=(
            FieldConfig("CUST_ID", "고객ID", "text", True, max_length=20),
            FieldConfig("LOG_DTTM", "로그일시", "datetime", True),
            FieldConfig("CHG_DVSN_CD", "변경구분코드", "text", True, max_length=1),
            FieldConfig("CHG_CONT", "변경내용", "text", max_length=4000),
            FieldConfig("PRCH_CONT", "구매내용", "text", max_length=1000),
            FieldConfig("PRCH_CONT1", "구매내용1", "text", max_length=1000),
            FieldConfig("CHG_DTM", "변경일시", "datetime", True),
            FieldConfig("CHG_ASET_NO", "변경자산번호", "text", True, max_length=20),
        ),
    ),
    "order-item": TableConfig(
        key="order-item",
        label="주문상품",
        schema="global_company",
        table="ORDER_ITEM",
        pk_fields=("ORD_NO", "PROD_ORD"),
        fields=(
            FieldConfig("ORD_NO", "주문번호", "text", True, max_length=20),
            FieldConfig("PROD_ORD", "상품순번", "number", True, scale=0),
            FieldConfig("PROD_CD", "상품코드", "text", True, max_length=20),
            FieldConfig("QTY", "수량", "number", True, scale=6),
            FieldConfig("UNPRC", "단가", "number", True, scale=2),
            FieldConfig("AMT", "금액", "number", True, scale=6),
            FieldConfig("REG_DTM", "등록일시", "datetime", True),
            FieldConfig("JOIN_DTTM", "가입일시", "datetime"),
            FieldConfig("JOIN_PATH_NM", "가입경로명", "text", max_length=100),
        ),
    ),
    "private-customer": TableConfig(
        key="private-customer",
        label="개인고객",
        schema="global_company",
        table="PRIVATE_CUSTOMER",
        pk_fields=("CSTNO",),
        fields=(
            FieldConfig("CSTNO", "고객번호", "number", True, scale=0),
            FieldConfig("CTRT_DAY", "계약일", "text", max_length=2),
            FieldConfig("REG_DTTM", "등록일시", "datetime"),
            FieldConfig("REG_EMPNO", "등록사원번호", "text", max_length=5),
            FieldConfig("MDFCN_DT", "수정일자", "date"),
            FieldConfig("MDFCN_EMPNO", "수정사원번호", "text", max_length=5),
        ),
    ),
    "private-product": TableConfig(
        key="private-product",
        label="개인상품",
        schema="global_company",
        table="PRIVATE_PRODUCT",
        pk_fields=("PROD_CD",),
        fields=(
            FieldConfig("PROD_CD", "상품코드", "text", True, max_length=30),
            FieldConfig("PROD_NM", "상품명", "text", True, max_length=500),
            FieldConfig("PRSN_ACHE_AMT", "개인실적금액", "number", True, scale=6),
            FieldConfig("REG_DTTM", "등록일시", "datetime"),
            FieldConfig("REG_EMPNO", "등록사원번호", "text", max_length=5),
        ),
    ),
    "product": TableConfig(
        key="product",
        label="상품",
        schema="global_company",
        table="PRODUCT",
        pk_fields=("PROD_CD",),
        fields=(
            FieldConfig("PROD_CD", "상품코드", "text", True, max_length=20),
            FieldConfig("PROD_NM", "상품명", "text", True, max_length=200),
            FieldConfig("PROD_DVSN_CD", "상품구분코드", "text", True, max_length=1),
            FieldConfig("NTSL_PRC", "판매가격", "number", True, scale=0),
            FieldConfig("STOCK_QTY", "재고수량", "number", True, scale=0),
            FieldConfig("USE_YN", "사용여부", "text", True, max_length=1),
            FieldConfig("REG_DTM", "등록일시", "datetime", True),
        ),
    ),
    "vip-customer": TableConfig(
        key="vip-customer",
        label="VIP고객",
        schema="global_company",
        table="VIP_CUSTOMER",
        pk_fields=("CUST_ID",),
        fields=(
            FieldConfig("GRAD_NO", "등급번호", "number", True, scale=0),
            FieldConfig("CUST_ID", "고객ID", "text", True, max_length=20),
            FieldConfig("RSVT_DSGN_DT", "예약지정일자", "date", True),
            FieldConfig("CFMTN_PIC_NM", "확정담당자명", "text", max_length=100),
            FieldConfig("CARD_BNFT_ID", "카드혜택ID", "number", scale=0),
            FieldConfig("REG_DTM", "등록일시", "datetime", True),
        ),
    ),
}


def get_table(table_key):
    try:
        return TABLES[table_key]
    except KeyError as exc:
        raise Http404("Unknown table.") from exc
