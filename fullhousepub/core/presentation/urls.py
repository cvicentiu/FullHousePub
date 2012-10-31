# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.presentation.views',
            url(r'list/$', 'file_upload', name='file_upload'),
            )
