from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from carts.models import Cart
from catalog.models import Categories, Products
from users.forms import UserLoginForm
from orders.models import Order
from users.models import User


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            "username": "user_1",
            "email": "user1@example.com",
            "first_name": "Firstname",
            "last_name": "Lastname",
            "password1": "23456789!Aa",
            "password2": "23456789!Aa",
        }

    def test_form_registration_get(self):
        path = reverse("users:registration")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "users/registration.html")

    # def test_user_registration_success(self):
    #     user_model = get_user_model()
    #     path = reverse('users:registration')
    #     session = self.client.session
    #     session['session_key'] = session.session_key or self.client.session.session_key
    #     session.save()

    #     product = Product.objects.create(
    #         product_id = 1,
    #         name = 'test',
    #         slug = 'test',
    #         description = 'test, test test',
    #         price = 13_000,
    #         quantity = 1,
    #         category = Category.objects.create(name="Standard"),
    #     )
    #     Cart.objects.create(session_key=session.session_key, product=product)

    #     response = self.client.post(path, self.data)
    #     self.assertEqual(response.status_code, HTTPStatus.FOUND)
    #     self.assertRedirects(response, reverse('users:profile'))

    #     user = user_model.objects.get(username=self.data['username'])
    #     self.assertTrue(Cart.objects.filter(user=user).exists())

    def test_user_registration_password_error(self):
        self.data["password2"] = "2345678A"
        path = reverse("users:registration")
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "The two password fields didn’t match.")

    def test_user_registration_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username=self.data["username"], password="testpass123"
        )

        path = reverse("users:registration")
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "A user with that username already exists.")


class LoginUserTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "Testpass123!"
        self.user = get_user_model().objects.create_user(
            username=self.username, password=self.password, email="test@example.com"
        )
        self.client = Client()

    # def test_login_get(self):
    #     response = self.client.get(reverse('users:login'))
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertTemplateUsed(response, 'users/login.html')

    # def test_login_success_and_cart_transfer(self):
    #     session = self.client.session
    #     session['session_key'] = session.session_key or self.client.session.session_key
    #     session.save()

    #     Cart.objects.create(session_key=session.session_key)

    #     response = self.client.post(
    #         reverse('users:login'),
    #         {'username': self.username, 'password': self.password}
    #     )

    # self.assertRedirects(response, reverse('main:index'))
    # self.assertTrue(Cart.objects.filter(user=self.user).exists())

    def test_login_failed(self):
        response = self.client.post(
            reverse("users:login"),
            {"username": self.username, "password": "WrongPass!"},
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Please enter a correct username and password.")


class UserProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user", password="Pass123456!", email="user@example.com"
        )
        self.client.login(username="user", password="Pass123456!")

    def test_profile_get(self):
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "users/profile.html")
        self.assertContains(response, "Profile")

    # def test_profile_update_success(self):
    #     response = self.client.post(reverse('users:profile'), {
    #         'first_name': 'Updated',
    #         'last_name': 'User',
    #         'email': 'new@example.com'
    #     })
    #     # self.assertRedirects(response, reverse('users:profile'))
    #     self.user.refresh_from_db()
    #     self.assertEqual(self.user.first_name, 'Updated')
    #     self.assertEqual(self.user.last_name, 'User')
    #     self.assertEqual(self.user.email, 'new@example.com')

    def test_profile_update_invalid(self):
        response = self.client.post(reverse("users:profile"), {"email": "not-an-email"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Enter a valid email address.")


class UserPasswordChangeTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user", email="user@example.com", password="OldPassword123!"
        )
        self.client.login(username="user", password="OldPassword123!")

    def test_change_password_success(self):
        response = self.client.post(
            reverse("users:password_change"),
            {
                "old_password": "OldPassword123!",
                "new_password1": "NewPassword123!",
                "new_password2": "NewPassword123!",
            },
        )
        self.assertRedirects(response, reverse("users:password_change_done"))

    def test_change_password_wrong_old(self):
        response = self.client.post(
            reverse("users:password_change"),
            {
                "old_password": "WrongOldPass!",
                "new_password1": "NewPassword123!",
                "new_password2": "NewPassword123!",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Your old password was entered incorrectly.")


"python manage.py test ."
"python manage.py test users"
