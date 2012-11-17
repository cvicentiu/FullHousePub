# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to
urlpatterns = patterns('interface.views',
            url(r'^$', redirect_to, {'url':'/menu/default/0/'}),
            url(r'^menu/(?P<subcat>\w+)/(?P<start_range>\d+)/$', 'menus', name='menus'),
            url(r'^offers/$', 'offers', name='offers'),
            url(r'^gallery/$', 'gallery', name='gallery'),
            url(r'^events/$', 'events', name='events'),
            url(r'^contact/$', 'contact', name='contact'),
            )
