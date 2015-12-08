import pytest

from django.http import Http404

from accession import admin_views

from .factories import DonorFactory, AccessionFactory

pytestmark = pytest.mark.django_db


class TestPrintView():

    def test_returns_200(self, rf, admin_user):
        DonorFactory()

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.print_view(request, 'accession', 'donor', 1)

        assert response.status_code == 200

    def test_raises_404_when_app_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.print_view(request, 'dne', 'dne', 1)

    def test_raises_404_when_model_does_not_exist(self, rf, admin_user):
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

    def test_raises_404_when_app_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.export_csv(request, 'dne', 'dne')

    def test_raises_404_when_model_does_not_exist(self, rf, admin_user):
        request = rf.get('/')
        request.user = admin_user

        with pytest.raises(Http404):
            admin_views.export_csv(request, 'accession', 'dne')

    def test_correct_info_returned(self, rf, admin_user):
        donors = DonorFactory.create_batch(10)

        request = rf.get('/')
        request.user = admin_user

        response = admin_views.export_csv(request, 'accession', 'donor')

        assert response.get('Content-Type') == 'text/csv'
        for donor in donors:
            assert str(donor.first_name) in response.content
            assert str(donor.last_name) in response.content

    def test_correct_info_returned_with_query_args(self, rf, admin_user):
        DonorFactory.create_batch(10, last_name='Henry')
        DonorFactory.create_batch(10, last_name='Fisher')

        request = rf.get('/?q=Henry')
        request.user = admin_user

        response = admin_views.export_csv(request, 'accession', 'donor')

        assert response.content.count('Henry') == 10
        assert response.content.count('Fisher') == 0

    def test_correct_info_returned_with_filters(self, rf, admin_user):
        AccessionFactory.create_batch(10, description='included',
                                      date_received='1990-01-01')
        AccessionFactory.create_batch(10, description='excluded',
                                      date_received='2000-05-05')

        request = rf.get('/?date_received__year=1990')
        request.user = admin_user

        response = admin_views.export_csv(request, 'accession', 'accession')

        assert response.content.count('included') == 10
        assert response.content.count('excluded') == 0
