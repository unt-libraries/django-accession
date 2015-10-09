from django.conf.urls import patterns, url, include
import django_databrowse
from accession.admin_views import duplicates, print_view
from djangosite.site_views import accession_admin

urlpatterns = patterns('',
    url(r'^databrowse/(.*)', django_databrowse.site.root),
    url(r'^admin/accession/(?P<model_selected>.*)/duplicates/$', duplicates),
    url(r'^admin/([^/]+)/([^/]+)/([0-9]+)/print/$', print_view),
    url(r'^admin/([^/]+)/([^/]+)/export_csv/$', 'csv_export.views.csv_view', name="tfc_csv_export"),
    url(r'^admin/', include(accession_admin.urls)),
)
