from http import HTTPStatus
from unittest.mock import patch
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from main.forms import ContactForm


User = get_user_model()

class MainViewsTestCase(TestCase):
    """
    Test suite for the views in the 'main' app: index and contact page.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up a test user for authentication-related tests. 
        Use setUpTestData to avoid recreating user for every test.
        """
        cls.user = User.objects.create_user(
            username='testuser',
            password='pass1234',
            first_name='Test',
            email='test@example.com',
        )

    def test_mainpage(self):
        """
        The homepage should return HTTP 200 and use the correct template and context.
        """
        path = reverse('main:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('main/index.html', response.template_name)
        self.assertEqual(response.context_data['title'], "The Best Motorcycles From The Best Store")
        self.assertEqual(response.context_data['content'], "FIND YOUR BIKE")

    def test_contactpage(self):
        """
        Contact page should return 200 and use the correct template.
        """
        path = reverse('main:contact')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'main/contact_form.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contactpage_get_with_authenticated_user(self):
        """
        Contact form should be pre-filled with authenticated user's data.
        """
        self.client.login(username='testuser', password='pass1234')
        path = reverse('main:contact')
        response = self.client.get(path)
        self.assertContains(response, 'value="Test"')
        self.assertContains(response, 'value="test@example.com"')

    def test_contact_form_post_valid_data(self):
        """
        Valid form submission should redirect and send an email.
        """
        data = {
            'first_name': 'Vladimir',
            'email': 'example@example.com',
            'message': 'Hello!',
        }
        path = reverse('main:contact')
        response = self.client.post(path, data)

        # Check redirect
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, path + '?success=1')

        # Check email was sent
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertIn('New Contact Message from Vladimir', email.subject)
        self.assertEqual(email.from_email, 'example@example.com')
        self.assertIn('Hello!', email.body)
        self.assertIn('neologfly@gmail.com', email.to)

    def test_contactpage_post_invalid_data(self):
        """
        Invalid form submission (e.g., missing fields) should not redirect.
        """
        data = {
            'first_name': '',  # Missing name
            'email': '',
            'message': '',
        }
        path = reverse('main:contact')
        response = self.client.post(path, data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    def test_contactpage_success_flag_in_context(self):
        """
        The 'success' flag in context should be True when ?success=1 is passed.
        """
        path = reverse('main:contact') + '?success=1'
        response = self.client.get(path)
        self.assertTrue(response.context['success'])

    def tearDown(self):
        """
        Clean-up actions after each test.
        """
        self.user.delete()


class ContactFormLoggingTestCase(TestCase):
    @patch('main.views.logger.info')
    def test_contact_form_logs_submission(self, mock_logger_info):
        """
        Ensure logger.info is called with correct arguments on valid form submission.
        """
        data = {
            'first_name': 'Vladimir',
            'email': 'vladimir@example.com',
            'message': 'Hello, this is a test!',
        }
        path = reverse('main:contact')
        response = self.client.post(path, data)

        # Redirect on successful post
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # Check logger was called once with expected message
        mock_logger_info.assert_called_once_with(
            "Contact form submitted by %s <%s>: %s",
            'Vladimir',
            'vladimir@example.com',
            'Hello, this is a test!'
        )

    @patch('main.views.logger.error')
    def test_contact_form_logs_error_on_invalid_submission(self, mock_logger_error):
        """
        Ensure logger.error is called when form submission fails with invalid data.
        """
        data = {
            'first_name': '',  # Missing required fields
            'email': '',
            'message': '',
        }
        path = reverse('main:contact')
        response = self.client.post(path, data)

        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Ensure logger.error was called once
        mock_logger_error.assert_called_once()

        # Extract arguments
        args, kwargs = mock_logger_error.call_args

        # Check format string and data passed to logger
        self.assertEqual(args[0], "Failed to submit contact form due to invalid data: %s")
        self.assertEqual(args[1], {
            'first_name': ['This field is required.'],
            'email': ['This field is required.'],
            'message': ['This field is required.'],
        })



# python manage.py test .
# python manage.py test main
