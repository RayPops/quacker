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
    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput, 
                                required=True, 
                                validators=[RegexValidator(
                                    regex='^[a-zA-Z0-9_]+$',
                                    message='Username may only contain alphanumeric characters or underscores.',
                                    code='invalid_username'
                                    )]            
    )
     
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 == password2:
            raise forms.ValidationError('Passwords do not match.')