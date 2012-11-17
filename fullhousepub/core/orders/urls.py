
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.orders.views',
            url(r'^buy/(?P<id>\d+)/$', 'process_buy', name='process_buy'),
            url(r'^clear/(?P<id>\d+)/$', 'clear_qty', name='clear_qty'),
            url(r'^update/$', 'update_qty', name='update_qty'),
            url(r'^finalise/$', 'finalise_order', name='finalise_order'),
            ) 
