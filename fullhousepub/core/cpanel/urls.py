# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.cpanel.views',
            url(r'^$', 'homepage', name='cpanel_homepage'),
            url(r'^users/$', 'view_users', name='users'),
            url(r'^menu/$', 'view_menu', name='menu'),
            url(r'^orders/$', 'view_orders', name='orders'),
            url(r'^images/$', 'view_images', name='images'),
            )
