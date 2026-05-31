from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import SalesOrders


class SalesOrdersListView(ListView):
    model = SalesOrders
    paginate_by = 20


class SalesOrdersDetailView(DetailView):
    model = SalesOrders


class SalesOrdersCreateView(CreateView):
    model = SalesOrders
    fields = "__all__"
    success_url = reverse_lazy("sales:list")


class SalesOrdersUpdateView(UpdateView):
    model = SalesOrders
    fields = "__all__"
    success_url = reverse_lazy("sales:list")


class SalesOrdersDeleteView(DeleteView):
    model = SalesOrders
    success_url = reverse_lazy("sales:list")
