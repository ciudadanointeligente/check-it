from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category
# Create your views here.

class HomeView(ListView):
    model = Category
    context_object_name = 'categories'
