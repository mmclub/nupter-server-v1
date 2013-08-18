# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from nuptsite.views import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	('^jwc/$', jwc),
    ('^jwc/new/$', jwc_new),

    ('^news/$', news),
    ('^news/new/$', news_new),

    ('^newspaper/$', newspaper),
    ('^newspaper/new$', newspaper_new),

    ('^lost/$', lost),
    ('^lost/new/$', lost_new),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


    )

