from django.contrib import admin

from .models import Customers, CustomerContacts, CustomerAddresses, CustomerSegments, CustomerConsents


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customers._meta.fields[:5]]
    search_fields = [field.name for field in Customers._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(CustomerContacts)
class CustomerContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerContacts._meta.fields[:5]]
    search_fields = [field.name for field in CustomerContacts._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(CustomerAddresses)
class CustomerAddressesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerAddresses._meta.fields[:5]]
    search_fields = [field.name for field in CustomerAddresses._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(CustomerSegments)
class CustomerSegmentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerSegments._meta.fields[:5]]
    search_fields = [field.name for field in CustomerSegments._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(CustomerConsents)
class CustomerConsentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerConsents._meta.fields[:5]]
    search_fields = [field.name for field in CustomerConsents._meta.fields if getattr(field, "max_length", None)][:3]
