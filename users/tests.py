from operator import ge
from django.contrib.auth import get_user_model
from django.test import TestCase


from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            'username': 'user_1',
            'email': 'user1@example.com',
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'password1': '23456789!Aa',
            'password2': '23456789!Aa',
        }

    def test_form_registration_get(self):
        path = reverse('users:registration')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_success(self):

        user_model = get_user_model()
        path = reverse('users:registration')
        response = self.client.post(path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:profile'))
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())

    def test_user_registration_password_error(self):
        self.data['password2'] = '2345678A'

        path = reverse('users:registration')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "The two password fields didn’t match.")

    def test_user_registragion_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create(username=self.data['username'])
        
        path = reverse('users:registration')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "A user with that username already exists.")

    def tearDown(self):
        "actions after test execution"



"python manage.py test ."
"python manage.py test users"
