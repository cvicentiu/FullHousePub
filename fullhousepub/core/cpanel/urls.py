# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.cpanel.views',
            url(r'^$', 'cpanel_homepage', name='cpanel_homepage'),
            url(r'^users/$', 'cpanel_homepage', name='users'),
            url(r'^menu/$', 'cpanel_homepage', name='menu'),
            url(r'^orders/$', 'cpanel_homepage', name='orders'),
            url(r'^images/$', 'cpanel_homepage', name='images'),
            url(r'^images/$', 'cpanel_homepage', name='presentation'),
            )
