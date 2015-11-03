import pytest

from django.http import Http404

from accession import admin_views

from .factories import DonorFactory, AccessionFactory

pytestmark = pytest.mark.django_db


class TestDuplicates():

    def test_returns_200_with_mapped_model(self, rf, admin_user):
        request = rf.get('/admin/accession/donor/duplicates/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert response.status_code == 200

    def test_returns_200_with_unmapped_model(self, rf, admin_user):
        request = rf.get('/admin/accession/donor/duplicates/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert response.status_code == 200

    @pytest.mark.xfail(reason='The view does not catch the exception raised'
                              'when the model does not exist')
    def test_returns_404_when_model_does_not_exist(self, rf, admin_user):
        request = rf.get('/admin/accession/donor/duplicates/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'dne')

        assert response.status_code == 404

    def test_template_used(self, admin_client):
        response = admin_client.get('/admin/accession/donor/duplicates/')
        assert response.templates[0].name == 'admin/accession/duplicates.html'

    def test_with_duplicates(self, rf, admin_user):
        # Non-duplicate entry
        DonorFactory(last_name='Libman')
        # Duplicate entries
        DonorFactory.create_batch(4, last_name='Smith')

        request = rf.get('/admin/accession/donor/duplicates/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert 'Libman' not in response.content
        assert 'Smith' in response.content

    def test_without_duplicates(self, rf, admin_user):
        DonorFactory.create_batch(5)

        request = rf.get('/admin/accession/donor/duplicates/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert 'There are no duplicate entries' in response.content


class TestPrintView():

    def test_returns_200(self, rf, admin_user):
        DonorFactory()

        request = rf.get('/admin/accession/donor/1/print/')
        request.user = admin_user

        response = admin_views.print_view(request, 'accession', 'donor', 1)

        assert response.status_code == 200

    def test_raises_404_when_object_id_not_found(self, rf, admin_user):
        request = rf.get('/admin/accession/donor/8/print/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.print_view(request, 'accession', 'donor', 8)

    def test_correct_info_printed(self, rf, admin_user):
        accession = AccessionFactory()

        request = rf.get('/admin/accession/accession/1/print/')
        request.user = admin_user

        response = admin_views.print_view(request, 'accession', 'accession', 1)

        # Check a couple fields to make sure they're there.
        assert accession.description in response.content
        assert accession.acquisition_method in response.content
        # Make sure the related items is there too.
        assert str(accession.donor) in response.content


def test_query_to_tuple():
    DonorFactory.create_batch(3, first_name='Bob', last_name='Tucker')

    query = """SELECT first_name, last_name from accession_donor"""
    expected = [('Bob', 'Tucker'), ('Bob', 'Tucker'), ('Bob', 'Tucker')]

    results = admin_views.query_to_tuple(query)

    assert results == expected


def test_query_to_tuple_no_results():
    query = """SELECT first_name, last_name from accession_donor"""
    expected = []

    results = admin_views.query_to_tuple(query)

    assert results == expected
