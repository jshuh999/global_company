from django.urls import path

from . import views

app_name = "organization"

urlpatterns = [
    path("", views.OrganizationsListView.as_view(), name="list"),
    path("create/", views.OrganizationsCreateView.as_view(), name="create"),
    path("<int:pk>/", views.OrganizationsDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.OrganizationsUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.OrganizationsDeleteView.as_view(), name="delete"),
]
