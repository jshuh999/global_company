from django.urls import path

from . import views

app_name = "common"

urlpatterns = [
    path("", views.CommonCodesListView.as_view(), name="list"),
    path("create/", views.CommonCodesCreateView.as_view(), name="create"),
    path("<int:pk>/", views.CommonCodesDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.CommonCodesUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.CommonCodesDeleteView.as_view(), name="delete"),
]
