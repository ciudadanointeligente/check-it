from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', HomeView.as_view(template_name='home.html', ), name='promises_home'),
)
