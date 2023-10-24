from django import forms
from django.contrib.auth.forms import UserCreationForm
from microblogs.models import User
from django.core.validators import RegexValidator

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio',)
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5}),
        }
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)