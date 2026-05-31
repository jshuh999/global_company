from django.db import models


class CommonCodes(models.Model):
    code_id = models.BigAutoField(primary_key=True)
    code_group = models.CharField(max_length=30)
    code_value = models.CharField(max_length=30)
    code_name = models.CharField(max_length=200)
    sort_order = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.common_codes"
        verbose_name = "공통코드"
        verbose_name_plural = "공통코드"

    def __str__(self):
        return str(self.code_name)
