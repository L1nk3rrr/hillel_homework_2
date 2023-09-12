import unittest

import app


class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_get_requirements(self):
        response = self.app.get('/requrements')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'blinker==1.6.2\n</br>certifi==2023.7.22\n', response.data)

    def test_get_requirements_beauty(self):
        response = self.app.get('/requrements_beauty')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>flask==2.3.3\n</h1>', response.data)

    def test_generate_users_default_qty(self):
        response = self.app.get('/generate-users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(100, len(response.text.split('</br>')))

    def test_generate_users_with_query_param(self):
        response = self.app.get('/generate-users/?qty=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(5, len(response.text.split('</br>')))

    def test_get_measurements_csv(self):
        response = self.app.get('/mean/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"172.70", response.data)

    def test_get_measurements_with_rounding_csv(self):
        response = self.app.get('/mean/?rounding=10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"172.7025085359", response.data)

    def test_get_number_spacers(self):
        response = self.app.get('/space/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"10", response.data)  # Replace with expected content
