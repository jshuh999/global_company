from django.db import models


class SalesOrders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=30)
    customer_id = models.BigIntegerField()
    cust_no = models.CharField(max_length=30)
    order_date = models.DateField(null=True, blank=True)
    order_status_code = models.CharField(max_length=30)
    order_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_orders"
        verbose_name = "판매주문"
        verbose_name_plural = "판매주문"

    def __str__(self):
        return str(self.order_id)

class SalesOrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    product_code = models.CharField(max_length=30)
    order_quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    order_unit_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    order_item_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_order_items"
        verbose_name = "판매주문상세"
        verbose_name_plural = "판매주문상세"

    def __str__(self):
        return str(self.order_item_id)

class SalesInvoices(models.Model):
    invoice_id = models.BigAutoField(primary_key=True)
    invoice_no = models.CharField(max_length=30)
    order_id = models.BigIntegerField()
    invoice_date = models.DateField(null=True, blank=True)
    invoice_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    invoice_status_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_invoices"
        verbose_name = "판매청구"
        verbose_name_plural = "판매청구"

    def __str__(self):
        return str(self.invoice_id)

class SalesPayments(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    invoice_id = models.BigIntegerField()
    payment_date = models.DateField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    payment_method_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_payments"
        verbose_name = "판매수금"
        verbose_name_plural = "판매수금"

    def __str__(self):
        return str(self.payment_id)

class SalesReturns(models.Model):
    return_id = models.BigAutoField(primary_key=True)
    return_no = models.CharField(max_length=30)
    order_id = models.BigIntegerField()
    return_date = models.DateField(null=True, blank=True)
    return_reason_code = models.CharField(max_length=30)
    return_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_returns"
        verbose_name = "판매반품"
        verbose_name_plural = "판매반품"

    def __str__(self):
        return str(self.return_id)

class SalesShipments(models.Model):
    shipment_id = models.BigAutoField(primary_key=True)
    shipment_no = models.CharField(max_length=30)
    order_id = models.BigIntegerField()
    shipment_date = models.DateField(null=True, blank=True)
    delivery_status_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_shipments"
        verbose_name = "판매출하"
        verbose_name_plural = "판매출하"

    def __str__(self):
        return str(self.shipment_id)

class SalesForecasts(models.Model):
    forecast_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    forecast_month = models.CharField(max_length=30)
    forecast_quantity = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    forecast_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_forecasts"
        verbose_name = "판매예측"
        verbose_name_plural = "판매예측"

    def __str__(self):
        return str(self.forecast_id)

class SalesChannels(models.Model):
    channel_id = models.BigAutoField(primary_key=True)
    channel_code = models.CharField(max_length=30)
    channel_name = models.CharField(max_length=200)
    channel_type_code = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_channels"
        verbose_name = "판매채널"
        verbose_name_plural = "판매채널"

    def __str__(self):
        return str(self.channel_name)
