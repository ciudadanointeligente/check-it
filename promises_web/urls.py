from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView, PromiseDetailView
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', HomeView.as_view(template_name='home.html', ), name='promises_home'),
        url(r'^promise/(?P<pk>[-\d]+)/?$', 
        	PromiseDetailView.as_view(template_name='promise_detail.html',), 
        	name = 'promise'),
)
