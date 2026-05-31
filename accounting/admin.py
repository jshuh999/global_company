from django.contrib import admin

from .models import AccountSubjects, FiscalPeriods, Vouchers, VoucherLines, Budgets, BudgetAllocations, TaxInvoices, MonthlyClosings


@admin.register(AccountSubjects)
class AccountSubjectsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AccountSubjects._meta.fields[:5]]
    search_fields = [field.name for field in AccountSubjects._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(FiscalPeriods)
class FiscalPeriodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FiscalPeriods._meta.fields[:5]]
    search_fields = [field.name for field in FiscalPeriods._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Vouchers)
class VouchersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vouchers._meta.fields[:5]]
    search_fields = [field.name for field in Vouchers._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(VoucherLines)
class VoucherLinesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VoucherLines._meta.fields[:5]]
    search_fields = [field.name for field in VoucherLines._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Budgets)
class BudgetsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Budgets._meta.fields[:5]]
    search_fields = [field.name for field in Budgets._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(BudgetAllocations)
class BudgetAllocationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BudgetAllocations._meta.fields[:5]]
    search_fields = [field.name for field in BudgetAllocations._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(TaxInvoices)
class TaxInvoicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TaxInvoices._meta.fields[:5]]
    search_fields = [field.name for field in TaxInvoices._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(MonthlyClosings)
class MonthlyClosingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MonthlyClosings._meta.fields[:5]]
    search_fields = [field.name for field in MonthlyClosings._meta.fields if getattr(field, "max_length", None)][:3]
