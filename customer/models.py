from django.db import models


class Customers(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    cust_no = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=200)
    customer_type_code = models.CharField(max_length=30)
    customer_status_code = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    gender_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.customers"
        verbose_name = "고객"
        verbose_name_plural = "고객"

    def __str__(self):
        return str(self.customer_name)

class CustomerContacts(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField()
    cust_no = models.CharField(max_length=30)
    contact_type_code = models.CharField(max_length=30)
    contact_value = models.CharField(max_length=200)
    is_primary = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.customer_contacts"
        verbose_name = "고객연락처"
        verbose_name_plural = "고객연락처"

    def __str__(self):
        return str(self.contact_id)

class CustomerAddresses(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField()
    address_type_code = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=200)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.customer_addresses"
        verbose_name = "고객주소"
        verbose_name_plural = "고객주소"

    def __str__(self):
        return str(self.address_id)

class CustomerSegments(models.Model):
    segment_id = models.BigAutoField(primary_key=True)
    segment_code = models.CharField(max_length=30)
    segment_name = models.CharField(max_length=200)
    segment_description = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.customer_segments"
        verbose_name = "고객세그먼트"
        verbose_name_plural = "고객세그먼트"

    def __str__(self):
        return str(self.segment_name)

class CustomerConsents(models.Model):
    consent_id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField()
    consent_type_code = models.CharField(max_length=30)
    is_consented = models.BooleanField(default=True)
    consented_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.customer_consents"
        verbose_name = "고객동의"
        verbose_name_plural = "고객동의"

    def __str__(self):
        return str(self.consent_id)
