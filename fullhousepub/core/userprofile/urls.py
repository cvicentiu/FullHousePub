from django.conf.urls.defaults import patterns, url
urlpatterns = patterns('core.userprofile.views',
            url(r'^login/$', 'login_parse', name='login_parse'),
            url(r'^logout/$', 'logout_parse', name='logout_parse'),
            url(r'^new/$', 'new_account', name='new_account'),
            url(r'^forgot/$', 'forgot_pass', name='forgot_pass'),
            url(r'^change/$', 'change_password', name='change_password'),
            )
