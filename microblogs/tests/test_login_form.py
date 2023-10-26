from django.test import TestCase
from django import forms
from microblogs.forms import LogInForm

class LogInFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
            'username': 'testuser',
            'password': 'testpass'
        }

    def test_form_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        password_field = form.fields['password']
        self.assertIsInstance(password_field.widget, forms.PasswordInput)

    def test_form_validation_for_valid_data(self):
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    
    def test_form_validation_for_blank_username(self):
        self.form_input['username'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_validation_for_blank_password(self):
        self.form_input['password'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())