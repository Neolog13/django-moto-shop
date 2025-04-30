from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def setUp(self):
        "initialization before executing the first test"

    def test_mainpage(self):
        path = reverse('main:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('main/index.html', response.template_name)
        self.assertEqual(response.context_data['title'], "The Best Motorcycles From The Best Store")

    def test_contactpage(self):
        path = reverse('main:contact')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'main/contact_form.html')

    def tearDown(self):
        "actions after test execution"



"python manage.py test ."
"python manage.py test main"
