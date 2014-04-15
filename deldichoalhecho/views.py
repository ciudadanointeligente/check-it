from django.shortcuts import render
from django.views.generic.list import ListView
from taggit.models import Tag
# Create your views here.

class HomeView(ListView):
    model = Tag
    context_object_name = 'tags'
