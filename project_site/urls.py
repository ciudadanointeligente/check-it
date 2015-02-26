from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('promises_web.urls')),
    url(r'^instances/', include('promises_instances.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# Your other patterns here
urlpatterns += [
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]