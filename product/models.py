from django.db import models


class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_code = models.CharField(max_length=30)
    product_name = models.CharField(max_length=200)
    product_type_code = models.CharField(max_length=30)
    product_status_code = models.CharField(max_length=30)
    list_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.products"
        verbose_name = "상품"
        verbose_name_plural = "상품"

    def __str__(self):
        return str(self.product_name)

class ProductCategories(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    parent_category_id = models.BigIntegerField()
    category_code = models.CharField(max_length=30)
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.product_categories"
        verbose_name = "상품분류"
        verbose_name_plural = "상품분류"

    def __str__(self):
        return str(self.category_name)

class ProductPrices(models.Model):
    price_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    sale_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    valid_from_date = models.DateField(null=True, blank=True)
    valid_to_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.product_prices"
        verbose_name = "상품가격"
        verbose_name_plural = "상품가격"

    def __str__(self):
        return str(self.price_id)

class ProductInventory(models.Model):
    inventory_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    warehouse_code = models.CharField(max_length=30)
    stock_quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    safety_quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.product_inventory"
        verbose_name = "상품재고"
        verbose_name_plural = "상품재고"

    def __str__(self):
        return str(self.inventory_id)

class ProductSuppliers(models.Model):
    supplier_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    supplier_code = models.CharField(max_length=30)
    supplier_name = models.CharField(max_length=200)
    business_no = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.product_suppliers"
        verbose_name = "상품공급사"
        verbose_name_plural = "상품공급사"

    def __str__(self):
        return str(self.supplier_name)

class ProductReviews(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    rating_score = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    review_contents = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.product_reviews"
        verbose_name = "상품리뷰"
        verbose_name_plural = "상품리뷰"

    def __str__(self):
        return str(self.review_id)
