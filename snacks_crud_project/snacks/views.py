from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"


class SnackDetailView(DetailView):
    model = Snack
    template_name = "snack_detail.html"


class SnackCreateView(CreateView):
    model = Snack
    template_name = "snack_create.html"
    fields = "__all__"


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = "snack_update.html"
    fields = "__all__"


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_delete.html"
    success_url = "/"
