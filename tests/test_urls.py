from django.core.urlresolvers import resolve

import django_databrowse

from accession import admin_views


def test_databrowse():
    assert resolve('/tfc/databrowse/').func == django_databrowse.site.root


def test_duplicates():
    assert resolve('/tfc/admin/accession/Objects/duplicates/').func == admin_views.duplicates


def test_print():
    assert resolve('/tfc/admin/accession/Objects/1/print/').func == admin_views.print_view
