from django.test import TestCase
from django.urls import reverse
from microblogs.forms import LogInForm

class LogInViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('login')
        self.get_url = self.client.get(self.url)
        self.form_input = {
            'username': 'testuser',
            'password': 'testpass'
        }

    def test_login_url(self):
        self.assertEqual(self.url, '/login/')

    def test_get_login_view(self):
        self.assertEqual(self.get_url.status_code, 200)

    def test_login_view_renders_login_template(self):
        self.assertTemplateUsed(self.get_url, 'login.html')

    def test_login_view_uses_login_form(self):
        form = self.get_url.context['form']
        self.assertIsInstance(form, LogInForm)
        

    