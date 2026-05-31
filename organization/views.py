from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Organizations


class OrganizationsListView(ListView):
    model = Organizations
    paginate_by = 20


class OrganizationsDetailView(DetailView):
    model = Organizations


class OrganizationsCreateView(CreateView):
    model = Organizations
    fields = "__all__"
    success_url = reverse_lazy("organization:list")


class OrganizationsUpdateView(UpdateView):
    model = Organizations
    fields = "__all__"
    success_url = reverse_lazy("organization:list")


class OrganizationsDeleteView(DeleteView):
    model = Organizations
    success_url = reverse_lazy("organization:list")
