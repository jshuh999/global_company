from django.contrib import admin
from django.urls import include, path

from common import views as common_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tables/", include("common.urls")),
    path("", common_views.table_index, name="home"),
]
