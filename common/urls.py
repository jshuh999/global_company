from django.urls import path, re_path

from . import views

app_name = "common"

urlpatterns = [
    path("", views.table_index, name="table-index"),
    path("<slug:table_key>/", views.table_list, name="table-list"),
    path("<slug:table_key>/create/", views.table_create, name="table-create"),
    re_path(r"^(?P<table_key>[-\w]+)/(?P<pk_path_value>.+)/edit/$", views.table_update, name="table-update"),
    re_path(r"^(?P<table_key>[-\w]+)/(?P<pk_path_value>.+)/delete/$", views.table_delete, name="table-delete"),
    re_path(r"^(?P<table_key>[-\w]+)/(?P<pk_path_value>.+)/$", views.table_detail, name="table-detail"),
]
