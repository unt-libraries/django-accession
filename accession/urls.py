from django.conf.urls import patterns, url, include
import django_databrowse

from accession.admin_views import duplicates, print_view, export_csv
from accession.site_views import accession_admin

urlpatterns = patterns(
    '',
    url(r'^databrowse/(.*)', django_databrowse.site.root),
    url(r'^admin/accession/(?P<model_selected>.*)/duplicates/$', duplicates),
    url(r'^admin/([^/]+)/([^/]+)/([0-9]+)/print/$', print_view),
    url(r'^admin/([^/]+)/([^/]+)/export_csv/$', export_csv, name="tfc_csv_export"),
    url(r'^admin/', include(accession_admin.urls)),
)
