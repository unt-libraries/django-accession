from django.conf.urls import patterns, include, url
from django.contrib import admin

from accession.admin_views import export_csv, print_view

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/(accession)/([^/]+)/([0-9]+)/print/$', print_view),
    url(r'^admin/(accession)/([^/]+)/export_csv/$', export_csv),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tfc/', include('accession.urls')),
)
