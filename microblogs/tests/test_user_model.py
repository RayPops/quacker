from django.test import TestCase
from microblogs.models import User

from django.core.exceptions import ValidationError

# User model tests
class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            bio='This is a test bio.'
        )

    def test_user_creation(self):
        self._assert_user_is_valid()

    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_cannot_be_null(self):
        self.user.username = None
        self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = 'a' * 30
        self._assert_user_is_valid()
    
    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = 'a' * 31
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        user2 = self._create_second_user()
        self.user.username = user2.username
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumeric_characters_and_underscores(self):
        self.user.username = 'test user'
        self._assert_user_is_invalid()

    def test_email_cannot_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()
    
    def test_email_cannot_be_null(self):
        self.user.email = None
        self._assert_user_is_invalid()
    
    def test_first_name_cannot_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()
    
    def test_first_name_cannot_be_null(self):
        self.user.first_name = None
        self._assert_user_is_invalid()

    def test_first_name_can_be_50_characters_long(self):
        self.user.first_name = 'a' * 50
        self._assert_user_is_valid()

    def test_first_name_cannot_be_over_50_characters_long(self):
        self.user.first_name = 'a' * 51
        self._assert_user_is_invalid()
    
    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_last_name_cannot_be_null(self):
        self.user.last_name = None
        self._assert_user_is_invalid()
    
    def test_last_name_can_be_50_characters_long(self):
        self.user.last_name = 'a' * 50
        self._assert_user_is_valid()
    
    def test_last_name_cannot_be_over_50_characters_long(self):
        self.user.last_name = 'a' * 51
        self._assert_user_is_invalid()

    def test_bio_can_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def test_email_is_validated(self):
        self.user.email = 'testuser'
        self._assert_user_is_invalid()

    def test_email_is_validated2(self):
        self.user.email = 'testuser@example'
        self._assert_user_is_invalid()

    def test_email_is_validated3(self):
        self.user.email = 'testuser@example.'
        self._assert_user_is_invalid()

    def test_email_is_validated4(self):
        self.user.email = 'testuserexample.c'
        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        user2 = self._create_second_user()
        self.user.email = user2.email
        self._assert_user_is_invalid()

    #Helper functions for easy testing
    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid.')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def _create_second_user(self):
        return User.objects.create_user(
            username='testuser2',
            password='testpass2',
            email='testuser2@example.com',
            first_name='Test',
            last_name='User',
            bio='This is a test bio.'
        )