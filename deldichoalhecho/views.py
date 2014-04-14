from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Promise
# Create your views here.

class HomeView(ListView):
    model = Promise
    context_object_name = 'promises'
