from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Products


class ProductsListView(ListView):
    model = Products
    paginate_by = 20


class ProductsDetailView(DetailView):
    model = Products


class ProductsCreateView(CreateView):
    model = Products
    fields = "__all__"
    success_url = reverse_lazy("product:list")


class ProductsUpdateView(UpdateView):
    model = Products
    fields = "__all__"
    success_url = reverse_lazy("product:list")


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy("product:list")
