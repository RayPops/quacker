from django.test import TestCase
from django.urls import reverse
from microblogs.forms import LogInForm
from microblogs.models import User
from .helpers import LogInTester

class LogInViewTestCase(TestCase, LogInTester):
    def setUp(self):
        self.url = reverse('login')
        self.get_url = self.client.get(self.url)
        self.form_input = {
            'username': 'testuser',
            'password': 'testpass'
        }
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            bio='This is a test bio.',
            is_active=True,
        )

    def test_login_url(self):
        self.assertEqual(self.url, '/login/')

    def test_get_login_view(self):
        self.assertEqual(self.get_url.status_code, 200)

    def test_login_view_renders_login_template(self):
        self.assertTemplateUsed(self.get_url, 'login.html')

    def test_login_view_uses_login_form(self):
        form = self.get_url.context['form']
        self.assertIsInstance(form, LogInForm)

    def test_unsuccessful_login(self):
        form_input = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        form = response.context['form']
        self.assertIsInstance(form, LogInForm)
        self.assertFalse(self._is_logged_in())

    def test_successful_login(self):
        response = self.client.post(self.url, self.form_input)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('feed'))
        self.assertTrue(self._is_logged_in())

    def test_valid_login_by_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.url, self.form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        form = response.context['form']
        self.assertIsInstance(form, LogInForm)
        self.assertFalse(self._is_logged_in())




    