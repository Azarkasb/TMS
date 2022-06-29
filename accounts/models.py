from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import phone_validator


class User(AbstractUser):
    phone = models.CharField(max_length=15, validators=[phone_validator], null=True, blank=True)

    @property
    def is_employer(self):
        return hasattr(self, 'employer')

    @property
    def is_employee(self):
        return hasattr(self, 'contractor')
