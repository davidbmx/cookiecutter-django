"""User Model"""

#django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#utilities
from {{ cookiecutter.project_slug }}.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """User model

    extiende de django abstract user para cambiar el username 
    y email y agrega estra fields
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with email already exists'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entrered in the format: +99999999999'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easyly distinguish users and perform queries.'
            'Clients are the main type of user.'            
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when user have verified its email address'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username