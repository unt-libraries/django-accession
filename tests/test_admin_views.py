import pytest

from django.http import Http404

from accession import admin_views

from .factories import DonorFactory, AccessionFactory

pytestmark = pytest.mark.django_db


class TestDuplicates():

    def test_returns_200_with_existing_model(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert response.status_code == 200

    def test_raises_404_when_model_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.duplicates(request, 'dne')

    def test_template_used(self, admin_client):
        response = admin_client.get('/admin/accession/donor/duplicates/')
        assert response.templates[0].name == 'admin/accession/duplicates.html'

    def test_with_duplicates(self, rf, admin_user):
        # Non-duplicate entry
        DonorFactory(last_name='Libman')
        # Duplicate entries
        DonorFactory.create_batch(4, last_name='Smith')

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert 'Libman' not in response.content
        assert 'Smith' in response.content

    def test_without_duplicates(self, rf, admin_user):
        DonorFactory.create_batch(5)

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.duplicates(request, 'donor')

        assert 'There are no duplicate entries' in response.content


class TestPrintView():

    def test_returns_200(self, rf, admin_user):
        DonorFactory()

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.print_view(request, 'accession', 'donor', 1)

        assert response.status_code == 200

    def test_returns_404_when_app_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.print_view(request, 'dne', 'dne', 1)

    def test_returns_404_when_model_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.print_view(request, 'accession', 'dne', 1)

    def test_raises_404_when_object_id_not_found(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.print_view(request, 'accession', 'donor', 8)

    def test_correct_info_printed(self, rf, admin_user):
        accession = AccessionFactory()

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.print_view(request, 'accession', 'accession', 1)

        # Check a couple fields to make sure they're there.
        assert accession.description in response.content
        assert accession.acquisition_method in response.content
        # Make sure the related items are there too.
        assert str(accession.donor) in response.content


class TestExportCsv():

    def test_returns_200(self, rf, admin_user):
        DonorFactory()

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.export_csv(request, 'accession', 'donor')

        assert response.status_code == 200

    def test_returns_404_when_app_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.export_csv(request, 'dne', 'dne')

    def test_returns_404_when_model_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.export_csv(request, 'accession', 'dne')

    def test_correct_info_returned(self, rf, admin_user):
        donors = DonorFactory.create_batch(10)

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.export_csv(request, 'accession', 'donor')

        for donor in donors:
            assert response.get('Content-Type') == 'text/csv'
            assert str(donor.first_name) in response.content
            assert str(donor.last_name) in response.content
