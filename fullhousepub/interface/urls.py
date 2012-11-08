# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('interface.views',
            url(r'^$', 'index', name='index'),
            url(r'^menu/$', 'menus', name='menus'),
            url(r'^offers/$', 'offers', name='offers'),
            url(r'^gallery/$', 'gallery', name='gallery'),
            url(r'^events/$', 'events', name='events'),
            url(r'^contact/$', 'contact', name='contact'),
            )
