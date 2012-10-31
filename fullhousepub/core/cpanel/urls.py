# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.cpanel.views',
            url(r'$', 'cpanel_homepage', name='cpanel_homepage'),
            )
