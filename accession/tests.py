import unittest
import requests
from djangosite import settings

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_databrowse_response_code(self):
        response = requests.get('http://%s/tfc/databrowse/' % settings.DOMAIN)
        self.assertEqual(response.status_code, 200)

    def test_admin_response_code(self):
        response = requests.get('http://%s/admin/accession/' % settings.DOMAIN)
        self.assertEqual(response.status_code, 200)

    def test_admin_duplicates_response_code(self):
        response = requests.get('http://%s/admin/accession/object/duplicates/' % settings.DOMAIN)
        self.assertEqual(response.status_code, 200)
