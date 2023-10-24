from django.test import TestCase
from microblogs.forms import SignupForm
from microblogs.models import User

from django.core.exceptions import ValidationError

class SignUpFormTestCase(TestCase):
    # Setup method
    def setUp(self):
        self.form_input = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'bio': 'This is a test bio.',
            'password1': 'testpass',
            'password2': 'testpass',
        }

    # Form accepts valid input data
    def test_form_accepts_valid_input(self):
        form = SignupForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    # Form has necessary fields
    def test_form_has_fields(self):
        form = SignupForm()
        expected_fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'password1', 'password2']
        actual_fields = list(form.fields)
        self.assertSequenceEqual(expected_fields, actual_fields)

    # Form enforces user model validations
    def test_form_enforces_user_model_validations(self):
        self.form_input['username'] = ''
        form = SignupForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    # Form checks password1 and password2 match
    def test_form_checks_passwords_match(self):
        self.form_input['password2'] = 'mismatch'
        form = SignupForm(data=self.form_input)
        self.assertFalse(form.is_valid())