from django.contrib import admin

from .models import Opportunities, Leads, Campaigns, CampaignResponses, SalesActivities, SalesTargets


@admin.register(Opportunities)
class OpportunitiesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Opportunities._meta.fields[:5]]
    search_fields = [field.name for field in Opportunities._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Leads._meta.fields[:5]]
    search_fields = [field.name for field in Leads._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(Campaigns)
class CampaignsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Campaigns._meta.fields[:5]]
    search_fields = [field.name for field in Campaigns._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(CampaignResponses)
class CampaignResponsesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CampaignResponses._meta.fields[:5]]
    search_fields = [field.name for field in CampaignResponses._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesActivities)
class SalesActivitiesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesActivities._meta.fields[:5]]
    search_fields = [field.name for field in SalesActivities._meta.fields if getattr(field, "max_length", None)][:3]

@admin.register(SalesTargets)
class SalesTargetsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalesTargets._meta.fields[:5]]
    search_fields = [field.name for field in SalesTargets._meta.fields if getattr(field, "max_length", None)][:3]
