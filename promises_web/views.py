from django.shortcuts import render
from django.views.generic.list import ListView
from promises.models import Category, Promise
from django.db.models import Avg
# Create your views here.

class HomeView(ListView):
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['summary'] = Promise.objects.all().summary()
        return context

    def get_queryset(self):
        queryset = super(HomeView, self).get_queryset()
        queryset = queryset.annotate(percentage = Avg('promises__fulfillment__percentage'))
        queryset = queryset.order_by('-percentage')
        return queryset
