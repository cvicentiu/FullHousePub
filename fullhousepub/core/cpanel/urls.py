# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.cpanel.views',
            url(r'^$', 'homepage', name='cpanel_homepage'),
            url(r'^fprofile/$', 'change_f_profile', name='change_f_profile'), 
            url(r'^jprofile/$', 'change_j_profile', name='change_j_profile'),
            url(r'^jprofile/(?P<uid>\d+)/$', 'change_j_profile', name='juridic_profile'),
            url(r'^aprofile/$', 'change_address_profile', name='change_address_profile'),
            url(r'^aprofile/(?P<uid>\d+)/$', 'change_address_profile', name='address_profile'),
            url(r'^orders/$', 'view_orders', name='view_orders'),
            url(r'^orders/(?P<order_id>\d+)/$', 'detail_order', name='detail_order'),
            url(r'^orders/(?P<order_id>\d+)/(?P<status>\d+)$', 'change_order',
                name='change_order'),


            url(r'^events/$', 'view_events', name='view_events'),
            url(r'^offers/$', 'view_offers', name='view_offers'),
            url(r'^users/$', 'view_users', name='view_users'),
            url(r'^menu/$', 'view_menu', name='view_menu'),
            url(r'^images/$', 'view_images', name='view_images'),
            
            url(r'^edit/(?P<what>\w+)/(?P<id>\d+)/$', 'edit_something',
                name='edit_something'),
            url(r'^delete/(?P<what>\w+)/(?P<id>\d+)/$', 'delete_something', 
                name='delete_something'),
            url(r'^add/(?P<what>\w+)/$', 'add_something', 
                name='add_something'),
            )
