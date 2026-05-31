from django.contrib import admin

from .models import CommonCodes


@admin.register(CommonCodes)
class CommonCodesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CommonCodes._meta.fields[:5]]
    search_fields = [field.name for field in CommonCodes._meta.fields if getattr(field, "max_length", None)][:3]
