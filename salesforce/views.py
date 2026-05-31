from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Opportunities


class OpportunitiesListView(ListView):
    model = Opportunities
    paginate_by = 20


class OpportunitiesDetailView(DetailView):
    model = Opportunities


class OpportunitiesCreateView(CreateView):
    model = Opportunities
    fields = "__all__"
    success_url = reverse_lazy("salesforce:list")


class OpportunitiesUpdateView(UpdateView):
    model = Opportunities
    fields = "__all__"
    success_url = reverse_lazy("salesforce:list")


class OpportunitiesDeleteView(DeleteView):
    model = Opportunities
    success_url = reverse_lazy("salesforce:list")
