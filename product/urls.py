from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="list"),
    path("create/", views.ProductsCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ProductsDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ProductsUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ProductsDeleteView.as_view(), name="delete"),
]
