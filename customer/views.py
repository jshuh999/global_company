from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Customers


class CustomersListView(ListView):
    model = Customers
    paginate_by = 20


class CustomersDetailView(DetailView):
    model = Customers


class CustomersCreateView(CreateView):
    model = Customers
    fields = "__all__"
    success_url = reverse_lazy("customer:list")


class CustomersUpdateView(UpdateView):
    model = Customers
    fields = "__all__"
    success_url = reverse_lazy("customer:list")


class CustomersDeleteView(DeleteView):
    model = Customers
    success_url = reverse_lazy("customer:list")
