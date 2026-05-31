from django.urls import path

from . import views

app_name = "customer"

urlpatterns = [
    path("", views.CustomersListView.as_view(), name="list"),
    path("create/", views.CustomersCreateView.as_view(), name="create"),
    path("<int:pk>/", views.CustomersDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.CustomersUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.CustomersDeleteView.as_view(), name="delete"),
]
