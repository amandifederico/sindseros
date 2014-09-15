from django.conf.urls import patterns, include, url
from django.contrib import admin
from gremio.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sindseros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index),
	url(r'^index.*/', index), 
)
