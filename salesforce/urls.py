from django.urls import path

from . import views

app_name = "salesforce"

urlpatterns = [
    path("", views.OpportunitiesListView.as_view(), name="list"),
    path("create/", views.OpportunitiesCreateView.as_view(), name="create"),
    path("<int:pk>/", views.OpportunitiesDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.OpportunitiesUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.OpportunitiesDeleteView.as_view(), name="delete"),
]
