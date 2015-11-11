import pytest

from accession.utils import ModelNotFound, find_duplicates

from .factories import DonorFactory

pytestmark = pytest.mark.django_db


class TestFindDuplicates():

    def test_raises_model_not_found(self):
        with pytest.raises(ModelNotFound):
            find_duplicates('dne')

    def test_returns_empty_list_if_no_duplicates(self):
        DonorFactory.create_batch(10)

        results = find_duplicates('donor')

        assert results == []

    def test_duplicates_found(self):
        DonorFactory.create_batch(3, last_name='Smith')
        DonorFactory.create_batch(7)
        DonorFactory.create_batch(4, last_name='Doe')

        results = find_duplicates('donor')

        expected = [(4, 'Doe'), (3, 'Smith')]

        assert results == expected
