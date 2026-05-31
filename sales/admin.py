from django.contrib import admin

from .models import SalesOrders, SalesOrderItems, SalesInvoices, SalesPayments, SalesReturns, SalesShipments, SalesForecasts, SalesChannels


@admin.register(SalesOrders)
class SalesOrdersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesOrders._meta.fields[:5]]
    search_fields = [field.name for field in SalesOrders._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesOrderItems)
class SalesOrderItemsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesOrderItems._meta.fields[:5]]
    search_fields = [field.name for field in SalesOrderItems._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesInvoices)
class SalesInvoicesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesInvoices._meta.fields[:5]]
    search_fields = [field.name for field in SalesInvoices._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesPayments)
class SalesPaymentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesPayments._meta.fields[:5]]
    search_fields = [field.name for field in SalesPayments._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesReturns)
class SalesReturnsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesReturns._meta.fields[:5]]
    search_fields = [field.name for field in SalesReturns._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesShipments)
class SalesShipmentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesShipments._meta.fields[:5]]
    search_fields = [field.name for field in SalesShipments._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesForecasts)
class SalesForecastsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesForecasts._meta.fields[:5]]
    search_fields = [field.name for field in SalesForecasts._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesChannels)
class SalesChannelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesChannels._meta.fields[:5]]
    search_fields = [field.name for field in SalesChannels._meta.fields if getattr(field, "max_length", None)][:3]
