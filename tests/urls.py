from django.conf.urls import patterns, include, url
from django.contrib import admin

from accession.admin_views import duplicates, export_csv, print_view
from accession.admin import main_admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/(accession)/([^/]+)/([0-9]+)/print/$', print_view),
    url(r'^admin/(accession)/(?P<model_selected>.*)/duplicates/$', duplicates),
    url(r'^admin/(accession)/([^/]+)/export_csv/$', export_csv),
    url(r'^admin/', include(main_admin.urls)),
    url(r'^tfc/', include('accession.urls')),
)
