from django.test import TestCase
from django.urls import reverse
from microblogs.forms import SignupForm
from .helpers import LogInTester

class SignUpViewTestCase(TestCase, LogInTester):
    def setUp(self):
        self.url = reverse('signup')
        self.get_url = self.client.get(self.url)
        self.form_input = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'bio': 'This is a test bio.',
            'password1': 'testpass',
            'password2': 'testpass',
        }

    def test_get_sign_up_view(self):
        self.assertEqual(self.get_url.status_code, 200)

    def test_signup_view_renders_signup_template(self):
        self.assertTemplateUsed(self.get_url, 'signup.html')

    def test_signup_view_uses_signup_form(self):
        form = self.get_url.context['form']
        self.assertIsInstance(form, SignupForm)

    def test_unsuccessful_signup(self):
        self.form_input['username'] = ''
        server_response = self.client.post(self.url, self.form_input)
        form = server_response.context['form']
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

    def test_successful_signup(self):
        server_response = self.client.post(self.url, self.form_input, follow=True)
        server_response_url = reverse('feed')
        self.assertRedirects(server_response, server_response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(server_response, 'feed.html')
        self.assertTrue(self._is_logged_in())