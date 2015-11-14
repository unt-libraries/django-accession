from django.conf.urls import patterns, include, url
from accession.admin_views import duplicates
from accession.admin import main_admin

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/accession/(?P<model_selected>.*)/duplicates/$', duplicates),
    url(r'^admin/', include(main_admin.urls)),
    url(r'^tfc/', include('accession.urls')),
)
