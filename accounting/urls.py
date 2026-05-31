from django.urls import path

from . import views

app_name = "accounting"

urlpatterns = [
    path("", views.AccountSubjectsListView.as_view(), name="list"),
    path("create/", views.AccountSubjectsCreateView.as_view(), name="create"),
    path("<int:pk>/", views.AccountSubjectsDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.AccountSubjectsUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.AccountSubjectsDeleteView.as_view(), name="delete"),
]
