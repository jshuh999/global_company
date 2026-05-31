from django.urls import path

from . import views

app_name = "sales"

urlpatterns = [
    path("", views.SalesOrdersListView.as_view(), name="list"),
    path("create/", views.SalesOrdersCreateView.as_view(), name="create"),
    path("<int:pk>/", views.SalesOrdersDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.SalesOrdersUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.SalesOrdersDeleteView.as_view(), name="delete"),
]
