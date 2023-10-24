from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=30, 
        unique=True,
        blank=False,
        # Add a validator to the username field, that checks that the username only contains alphanumeric characters or underscores.
        validators=[RegexValidator(
                regex='^[a-zA-Z0-9_]+$',
                message='Username may only contain alphanumeric characters or underscores.',
                code='invalid_username'
            )]            
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)