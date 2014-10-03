from django.conf.urls import patterns, include, url
from django.contrib import * #admin
from gremio.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sindseros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index),
	url(r'^index/', index),
	url(r'^menu/', menu), 
	url(r'^contacts/', contacto), 
	url(r'^afiliado/$', afiliado),
        url(r'^abmafiliado/(\d+)$',abmAfiliado),
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^registration/logged_out.html$',logout),
)
