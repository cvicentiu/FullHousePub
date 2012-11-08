from django.conf.urls.defaults import patterns, url
urlpatterns = patterns('core.userprofile.views',
            url(r'^$', 'login_parse', name='login_parse'),
            url(r'^new/$', 'new_account', name='new_account')
            )
