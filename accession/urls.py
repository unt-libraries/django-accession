from django.conf.urls import url, include

from accession.admin_views import duplicates, print_view, export_csv
from accession.admin import accession_admin

urlpatterns = [
    url(r'^admin/accession/(?P<model_selected>.*)/duplicates/$', duplicates),
    url(r'^admin/([^/]+)/([^/]+)/([0-9]+)/print/$', print_view),
    url(r'^admin/([^/]+)/([^/]+)/export_csv/$', export_csv, name="tfc_csv_export"),
    url(r'^admin/', include(accession_admin.urls)),
]
