# Global Company Django 업무 시스템

Data Governance 리니지 검증용 Django 업무 웹 시스템입니다.

## 구성

- Django project: global_company
- 업무 app: common, customer, product, sales, salesforce, organization, accounting
- DB schema: global_company
- 명시적 SQL: sql/lineage_queries.sql, sql/mybatis/customer_mapper.xml, common/repositories.py

## 실행

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
copy .env.example .env
python manage.py runserver
```

실제 DB password는 .env에만 두고 commit하지 않습니다.
