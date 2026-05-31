from django.contrib import admin

from .models import Organizations, Departments, Employees, Positions, EmployeeAssignments, ApprovalLines


@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Organizations._meta.fields[:5]]
    search_fields = [field.name for field in Organizations._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Departments._meta.fields[:5]]
    search_fields = [field.name for field in Departments._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employees._meta.fields[:5]]
    search_fields = [field.name for field in Employees._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Positions._meta.fields[:5]]
    search_fields = [field.name for field in Positions._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(EmployeeAssignments)
class EmployeeAssignmentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployeeAssignments._meta.fields[:5]]
    search_fields = [field.name for field in EmployeeAssignments._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(ApprovalLines)
class ApprovalLinesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ApprovalLines._meta.fields[:5]]
    search_fields = [field.name for field in ApprovalLines._meta.fields if getattr(field, "max_length", None)][:3]
