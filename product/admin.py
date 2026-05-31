from django.contrib import admin

from .models import Products, ProductCategories, ProductPrices, ProductInventory, ProductSuppliers, ProductReviews


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.fields[:5]]
    search_fields = [field.name for field in Products._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(ProductCategories)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategories._meta.fields[:5]]
    search_fields = [field.name for field in ProductCategories._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(ProductPrices)
class ProductPricesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductPrices._meta.fields[:5]]
    search_fields = [field.name for field in ProductPrices._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInventory._meta.fields[:5]]
    search_fields = [field.name for field in ProductInventory._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(ProductSuppliers)
class ProductSuppliersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductSuppliers._meta.fields[:5]]
    search_fields = [field.name for field in ProductSuppliers._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductReviews._meta.fields[:5]]
    search_fields = [field.name for field in ProductReviews._meta.fields if getattr(field, "max_length", None)][:3]
