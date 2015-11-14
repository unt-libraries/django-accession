from django.core.urlresolvers import resolve

from accession import admin_views


def test_duplicates():
    assert resolve('/tfc/admin/accession/Objects/duplicates/').func == admin_views.duplicates


def test_print():
    assert resolve('/tfc/admin/accession/Objects/1/print/').func == admin_views.print_view


def test_export_csv():
    assert resolve('/tfc/admin/accession/Objects/export_csv/').func == admin_views.export_csv
