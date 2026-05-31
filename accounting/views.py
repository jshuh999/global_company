from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import AccountSubjects


class AccountSubjectsListView(ListView):
    model = AccountSubjects
    paginate_by = 20


class AccountSubjectsDetailView(DetailView):
    model = AccountSubjects


class AccountSubjectsCreateView(CreateView):
    model = AccountSubjects
    fields = "__all__"
    success_url = reverse_lazy("accounting:list")


class AccountSubjectsUpdateView(UpdateView):
    model = AccountSubjects
    fields = "__all__"
    success_url = reverse_lazy("accounting:list")


class AccountSubjectsDeleteView(DeleteView):
    model = AccountSubjects
    success_url = reverse_lazy("accounting:list")
