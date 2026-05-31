from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import CommonCodes


class CommonCodesListView(ListView):
    model = CommonCodes
    paginate_by = 20


class CommonCodesDetailView(DetailView):
    model = CommonCodes


class CommonCodesCreateView(CreateView):
    model = CommonCodes
    fields = "__all__"
    success_url = reverse_lazy("common:list")


class CommonCodesUpdateView(UpdateView):
    model = CommonCodes
    fields = "__all__"
    success_url = reverse_lazy("common:list")


class CommonCodesDeleteView(DeleteView):
    model = CommonCodes
    success_url = reverse_lazy("common:list")
