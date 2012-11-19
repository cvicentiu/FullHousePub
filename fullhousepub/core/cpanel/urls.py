# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.cpanel.views',
            url(r'^$', 'homepage', name='cpanel_homepage'),
            url(r'^jprofile/$', 'view_j_profile', name='view_j_profile'),
            url(r'^orders/(?P<order_id>\d+)/$', 'view_orders', name='view_orders'),
            url(r'^orders/d/(?P<order_id>\d+)/$', 'detail_order', name='detail_order'),
            url(r'^orders/d/(?P<order_id>\d+)/(?P<status>\d+)$', 'change_order',
                name='change_order'),


            url(r'^events/$', 'view_events', name='view_events'),
            url(r'^offers/$', 'view_offers', name='view_offers'),
            url(r'^users/$', 'view_users', name='view_users'),
            url(r'^menu/$', 'view_menu', name='view_menu'),
            url(r'^images/$', 'view_images', name='view_images'),
            url(r'^contacts/$', 'view_contacts', name='view_contacts'),
            
            url(r'^edit/(?P<what>\w+)/(?P<id>\d+)/$', 'edit_something',
                name='edit_something'),
            url(r'^delete/(?P<what>\w+)/(?P<id>\d+)/$', 'delete_something', 
                name='delete_something'),
            url(r'^add/(?P<what>\w+)/$', 'add_something', 
                name='add_something'),
            )
