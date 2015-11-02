import pytest

from accession import admin_views

from .factories import DonorFactory

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

    def test_status_ok(self, rf, admin_user):
        pass


def test_query_to_tuple():
    pass


def test_query_to_tuple_no_results():
    pass
