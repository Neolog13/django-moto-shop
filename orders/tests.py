from urllib import response
from django.test import TestCase

from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse



class GetPagesTestCase(TestCase):
    def setUp(self):
        "initialization before executing the first test"

    def test_redirect_addpage(self):
        path = reverse('orders:create_order')
        redirect_url = reverse('users:login') + '?next=' + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_url)

    def tearDown(self):
        "actions after test execution"



"python manage.py test ."
"python manage.py test orders"
