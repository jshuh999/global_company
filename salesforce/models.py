from django.db import models


class Opportunities(models.Model):
    opportunity_id = models.BigAutoField(primary_key=True)
    opportunity_no = models.CharField(max_length=30)
    customer_id = models.BigIntegerField()
    opportunity_name = models.CharField(max_length=200)
    stage_code = models.CharField(max_length=30)
    expected_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.opportunities"
        verbose_name = "영업기회"
        verbose_name_plural = "영업기회"

    def __str__(self):
        return str(self.opportunity_name)

class Leads(models.Model):
    lead_id = models.BigAutoField(primary_key=True)
    lead_no = models.CharField(max_length=30)
    lead_name = models.CharField(max_length=200)
    lead_source_code = models.CharField(max_length=30)
    lead_status_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.leads"
        verbose_name = "리드"
        verbose_name_plural = "리드"

    def __str__(self):
        return str(self.lead_name)

class Campaigns(models.Model):
    campaign_id = models.BigAutoField(primary_key=True)
    campaign_code = models.CharField(max_length=30)
    campaign_name = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    campaign_budget = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.campaigns"
        verbose_name = "캠페인"
        verbose_name_plural = "캠페인"

    def __str__(self):
        return str(self.campaign_name)

class CampaignResponses(models.Model):
    response_id = models.BigAutoField(primary_key=True)
    campaign_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    response_type_code = models.CharField(max_length=30)
    responded_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.campaign_responses"
        verbose_name = "캠페인반응"
        verbose_name_plural = "캠페인반응"

    def __str__(self):
        return str(self.response_id)

class SalesActivities(models.Model):
    activity_id = models.BigAutoField(primary_key=True)
    employee_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    activity_type_code = models.CharField(max_length=30)
    activity_at = models.DateTimeField(null=True, blank=True)
    activity_summary = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_activities"
        verbose_name = "영업활동"
        verbose_name_plural = "영업활동"

    def __str__(self):
        return str(self.activity_id)

class SalesTargets(models.Model):
    target_id = models.BigAutoField(primary_key=True)
    employee_id = models.BigIntegerField()
    target_month = models.CharField(max_length=30)
    target_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    actual_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.sales_targets"
        verbose_name = "영업목표"
        verbose_name_plural = "영업목표"

    def __str__(self):
        return str(self.target_id)
