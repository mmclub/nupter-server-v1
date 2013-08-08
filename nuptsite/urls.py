from django.conf.urls import patterns, include, url
from nuptsite.views import *
from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^index/$', index),
	('^header/$', header),
    # Examples:
    # url(r'^$', 'nuptsite.views.home', name='home'),
    # url(r'^nuptsite/', include('nuptsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),


)

