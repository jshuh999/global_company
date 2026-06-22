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
        table="customer",
        pk_fields=("cst_id",),
        fields=(
            FieldConfig("cst_nm", "고객명", "text", True, max_length=50),
            FieldConfig("cst_id", "고객ID", "text", True, max_length=20),
            FieldConfig("eaddr", "이메일주소", "text", max_length=200),
            FieldConfig("telno", "전화번호", "text", max_length=20),
            FieldConfig("brdt", "생년월일", "date"),
            FieldConfig("grad_cd", "등급코드", "text", max_length=2),
            FieldConfig("cst_addr1", "고객주소", "text", max_length=1000),
            FieldConfig("join_dttm", "가입일시", "datetime"),
            FieldConfig("last_lgn_dttm", "최종로그인일시", "datetime"),
            FieldConfig("use_yn", "사용여부", "text", True, max_length=1),
            FieldConfig("reg_dttm", "등록일시", "datetime", True),
        ),
    ),
    "customer-addr": TableConfig(
        key="customer-addr",
        label="고객주소",
        schema="global_company",
        table="customer_addr",
        pk_fields=("cst_id", "cst_addr"),
        fields=(
            FieldConfig("cst_id", "고객ID", "text", True, max_length=20),
            FieldConfig("cst_addr", "고객주소", "text", True, max_length=1000),
            FieldConfig("addr_nm", "주소명", "text", True, max_length=100),
            FieldConfig("zipno", "우편번호", "text", max_length=6),
            FieldConfig("rslt_addr", "결과주소1", "text", max_length=300),
            FieldConfig("rslt_addr2", "결과주소2", "text", max_length=300),
            FieldConfig("use_yn", "사용여부", "text", True, max_length=1),
            FieldConfig("reg_dttm", "등록일시", "datetime", True),
            FieldConfig("rgtr_nm", "등록자명", "text", True, max_length=500),
        ),
    ),
    "customer-log": TableConfig(
        key="customer-log",
        label="고객변경로그",
        schema="global_company",
        table="customer_log",
        pk_fields=("log_dttm",),
        readonly=True,
        fields=(
            FieldConfig("cst_id", "고객ID", "text", True, max_length=20),
            FieldConfig("log_dttm", "로그일시", "datetime", True),
            FieldConfig("chg_dvsn_cd", "변경구분코드", "text", True, max_length=1),
            FieldConfig("chg_cont", "변경내용", "text", max_length=4000),
            FieldConfig("prch_cont", "구매내용", "text", max_length=1000),
            FieldConfig("chg_dttm", "변경일시", "datetime", True),
            FieldConfig("chg_aset_no", "변경자산번호", "text", True, max_length=20),
        ),
    ),
    "order-item": TableConfig(
        key="order-item",
        label="주문상품",
        schema="global_company",
        table="order_item",
        pk_fields=("ord_no", "prod_ord"),
        fields=(
            FieldConfig("ord_no", "주문번호", "text", True, max_length=20),
            FieldConfig("prod_ord", "상품순번", "number", True, scale=0),
            FieldConfig("prod_cd", "상품코드", "text", True, max_length=20),
            FieldConfig("qty", "수량", "number", True, scale=6),
            FieldConfig("unprc", "단가", "number", True, scale=2),
            FieldConfig("amt", "금액", "number", True, scale=6),
            FieldConfig("reg_dtm", "등록일시", "datetime", True),
            FieldConfig("join_dttm", "가입일시", "datetime"),
            FieldConfig("join_path_nm", "가입경로명", "text", max_length=100),
        ),
    ),
    "private-customer": TableConfig(
        key="private-customer",
        label="개인고객",
        schema="global_company",
        table="private_customer",
        pk_fields=("cstno",),
        fields=(
            FieldConfig("cstno", "고객번호", "number", True, scale=0),
            FieldConfig("ctrt_day", "계약일", "text", max_length=2),
            FieldConfig("reg_dttm", "등록일시", "datetime"),
            FieldConfig("mdfcn_dt", "수정일자", "date"),
            FieldConfig("mdfcn_empno", "수정사원번호", "text", max_length=5),
        ),
    ),
    "private-product": TableConfig(
        key="private-product",
        label="개인상품",
        schema="global_company",
        table="private_product",
        pk_fields=("prod_cd",),
        fields=(
            FieldConfig("prod_cd", "상품코드", "text", True, max_length=30),
            FieldConfig("prod_nm", "상품명", "text", True, max_length=500),
            FieldConfig("prsn_ache_amt", "개인실적금액", "number", True, scale=6),
            FieldConfig("reg_dttm", "등록일시", "datetime"),
            FieldConfig("reg_empno", "등록사원번호", "text", max_length=5),
        ),
    ),
    "product": TableConfig(
        key="product",
        label="상품",
        schema="global_company",
        table="product",
        pk_fields=("prod_cd",),
        fields=(
            FieldConfig("prod_cd", "상품코드", "text", True, max_length=20),
            FieldConfig("prod_nm", "상품명", "text", True, max_length=200),
            FieldConfig("prod_dvsn_cd", "상품구분코드", "text", True, max_length=1),
            FieldConfig("ntsl_prc", "판매가격", "number", True, scale=0),
            FieldConfig("stock_qty", "재고수량", "number", True, scale=0),
            FieldConfig("use_yn", "사용여부", "text", True, max_length=1),
            FieldConfig("reg_dtm", "등록일시", "datetime", True),
        ),
    ),
    "vip-customer": TableConfig(
        key="vip-customer",
        label="VIP고객",
        schema="global_company",
        table="vip_customer",
        pk_fields=("cst_id",),
        fields=(
            FieldConfig("grad_no", "등급번호", "number", True, scale=0),
            FieldConfig("cst_id", "고객ID", "text", True, max_length=20),
            FieldConfig("rsvt_dsgn_dt", "예약지정일자", "date", True),
            FieldConfig("cfmtn_pic_nm", "확정담당자명", "text", max_length=100),
            FieldConfig("card_bnft_id", "카드혜택ID", "number", scale=0),
            FieldConfig("reg_dttm", "등록일시", "datetime", True),
        ),
    ),
}


def get_table(table_key):
    try:
        return TABLES[table_key]
    except KeyError as exc:
        raise Http404("Unknown table.") from exc
