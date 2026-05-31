from django.db import models


class AccountSubjects(models.Model):
    account_subject_id = models.BigAutoField(primary_key=True)
    account_subject_code = models.CharField(max_length=30)
    account_subject_name = models.CharField(max_length=200)
    account_type_code = models.CharField(max_length=30)
    is_postable = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.account_subjects"
        verbose_name = "계정과목"
        verbose_name_plural = "계정과목"

    def __str__(self):
        return str(self.account_subject_name)

class FiscalPeriods(models.Model):
    fiscal_period_id = models.BigAutoField(primary_key=True)
    fiscal_year = models.CharField(max_length=30)
    period_code = models.CharField(max_length=30)
    period_start_date = models.DateField(null=True, blank=True)
    period_end_date = models.DateField(null=True, blank=True)
    is_closed = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.fiscal_periods"
        verbose_name = "회계기간"
        verbose_name_plural = "회계기간"

    def __str__(self):
        return str(self.fiscal_period_id)

class Vouchers(models.Model):
    voucher_id = models.BigAutoField(primary_key=True)
    voucher_no = models.CharField(max_length=30)
    voucher_date = models.DateField(null=True, blank=True)
    voucher_type_code = models.CharField(max_length=30)
    voucher_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    approval_status_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.vouchers"
        verbose_name = "전표"
        verbose_name_plural = "전표"

    def __str__(self):
        return str(self.voucher_id)

class VoucherLines(models.Model):
    voucher_line_id = models.BigAutoField(primary_key=True)
    voucher_id = models.BigIntegerField()
    account_subject_id = models.BigIntegerField()
    debit_credit_code = models.CharField(max_length=30)
    line_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    line_description = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.voucher_lines"
        verbose_name = "전표상세"
        verbose_name_plural = "전표상세"

    def __str__(self):
        return str(self.voucher_line_id)

class Budgets(models.Model):
    budget_id = models.BigAutoField(primary_key=True)
    budget_year = models.CharField(max_length=30)
    department_id = models.BigIntegerField()
    budget_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    budget_status_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.budgets"
        verbose_name = "예산"
        verbose_name_plural = "예산"

    def __str__(self):
        return str(self.budget_id)

class BudgetAllocations(models.Model):
    allocation_id = models.BigAutoField(primary_key=True)
    budget_id = models.BigIntegerField()
    account_subject_id = models.BigIntegerField()
    allocated_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    used_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.budget_allocations"
        verbose_name = "예산배정"
        verbose_name_plural = "예산배정"

    def __str__(self):
        return str(self.allocation_id)

class TaxInvoices(models.Model):
    tax_invoice_id = models.BigAutoField(primary_key=True)
    tax_invoice_no = models.CharField(max_length=30)
    issue_date = models.DateField(null=True, blank=True)
    vendor_name = models.CharField(max_length=200)
    supply_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.tax_invoices"
        verbose_name = "세금계산서"
        verbose_name_plural = "세금계산서"

    def __str__(self):
        return str(self.vendor_name)

class MonthlyClosings(models.Model):
    closing_id = models.BigAutoField(primary_key=True)
    closing_month = models.CharField(max_length=30)
    closing_status_code = models.CharField(max_length=30)
    closed_at = models.DateTimeField(null=True, blank=True)
    closing_description = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.monthly_closings"
        verbose_name = "월마감"
        verbose_name_plural = "월마감"

    def __str__(self):
        return str(self.closing_id)
