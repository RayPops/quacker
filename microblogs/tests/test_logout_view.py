from django.test import TestCase
from django.urls import reverse
from microblogs.models import User
from .helpers import LogInTester

class LogOutViewTestCase(TestCase, LogInTester):
    def setUp(self):
        self.url = reverse('logout')
        self.get_url = self.client.get(self.url)
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            first_name='Test',
            last_name='User',
            email='testuser@example.org',
            bio='This is a test bio.',
            is_active=True,
        )

    def test_logout_url(self):
        self.assertEqual(self.url, '/logout/')

    def test_get_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        self.assertTrue(self._is_logged_in())
        response = self.client.get(self.url, follow=True)
        response_url = reverse('home')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertFalse(self._is_logged_in())