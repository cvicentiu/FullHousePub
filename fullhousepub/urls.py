from django.conf.urls.defaults import *
from fullhousepub import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('interface.urls')),
    (r'^upload/', include('core.presentation.urls')),
    (r'^cpanel/', include('core.cpanel.urls')),
    (r'^auth/', include('core.userprofile.urls')),
    (r'^order/', include('core.orders.urls')),
    # Example:
    # (r'^fullhousepub/', include('fullhousepub.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT  })
    )
