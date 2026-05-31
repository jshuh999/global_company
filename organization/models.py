from django.db import models


class Organizations(models.Model):
    organization_id = models.BigAutoField(primary_key=True)
    organization_code = models.CharField(max_length=30)
    organization_name = models.CharField(max_length=200)
    organization_type_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.organizations"
        verbose_name = "회사조직"
        verbose_name_plural = "회사조직"

    def __str__(self):
        return str(self.organization_name)

class Departments(models.Model):
    department_id = models.BigAutoField(primary_key=True)
    organization_id = models.BigIntegerField()
    parent_department_id = models.BigIntegerField()
    department_code = models.CharField(max_length=30)
    department_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.departments"
        verbose_name = "부서"
        verbose_name_plural = "부서"

    def __str__(self):
        return str(self.department_name)

class Employees(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    employee_no = models.CharField(max_length=30)
    employee_name = models.CharField(max_length=200)
    department_id = models.BigIntegerField()
    employment_status_code = models.CharField(max_length=30)
    hire_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.employees"
        verbose_name = "사원"
        verbose_name_plural = "사원"

    def __str__(self):
        return str(self.employee_name)

class Positions(models.Model):
    position_id = models.BigAutoField(primary_key=True)
    position_code = models.CharField(max_length=30)
    position_name = models.CharField(max_length=200)
    position_level_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.positions"
        verbose_name = "직위"
        verbose_name_plural = "직위"

    def __str__(self):
        return str(self.position_name)

class EmployeeAssignments(models.Model):
    assignment_id = models.BigAutoField(primary_key=True)
    employee_id = models.BigIntegerField()
    department_id = models.BigIntegerField()
    position_id = models.BigIntegerField()
    effective_from_date = models.DateField(null=True, blank=True)
    effective_to_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.employee_assignments"
        verbose_name = "사원발령"
        verbose_name_plural = "사원발령"

    def __str__(self):
        return str(self.assignment_id)

class ApprovalLines(models.Model):
    approval_line_id = models.BigAutoField(primary_key=True)
    approval_type_code = models.CharField(max_length=30)
    requester_employee_id = models.BigIntegerField()
    approver_employee_id = models.BigIntegerField()
    approval_order = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = "global_company.approval_lines"
        verbose_name = "결재선"
        verbose_name_plural = "결재선"

    def __str__(self):
        return str(self.approval_line_id)
