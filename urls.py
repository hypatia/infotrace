from django.conf.urls.defaults import *
from infotrace.views import current_datetime

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^infotrace/', include('infotrace.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^time/$', current_datetime),
)
