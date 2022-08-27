from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Snack


class SnackListView(ListView):
    """
    To show the snacks in a list
    """
    template_name = "snack_list.html"
    model = Snack


class SnackDetailView(DetailView):
    """
    To show the snack detail in a list
    """
    template_name = "snack_detail.html"
    model = Snack
