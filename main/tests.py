from django.test import TestCase
import requests


class OSStatisticTest(TestCase):
    url = "http://127.0.0.1:8000/"
    headers = {}

    def setUp(self):

        response = requests.post(
            self.url + "auth-token/", data={"username": "Jamshid", "password": "1"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.token = data['token']
        self.headers["Authorization"] = "Token " + self.token

    def test_os_diagram(self):
        response = requests.get(self.url + "api/main/os-diagram/", headers=self.headers)
        data = response.json()
        self.assertIsInstance(data, dict)

    def test_increase_e_commerce(self):
        response = requests.get(self.url + "api/main/increase", headers=self.headers)
        data = response.json()
        if data:
            self.assertIsInstance(data[0], cls=dict)
            self.assertEqual(len(data[0].keys()), 2)






