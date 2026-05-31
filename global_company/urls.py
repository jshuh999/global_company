from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("customer/", include("customer.urls")),
    path("product/", include("product.urls")),
    path("sales/", include("sales.urls")),
    path("salesforce/", include("salesforce.urls")),
    path("organization/", include("organization.urls")),
    path("accounting/", include("accounting.urls")),
]
