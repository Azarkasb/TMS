from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import phone_validator


class User(AbstractUser):
    phone = models.CharField(
        max_length=15, validators=[phone_validator], null=True, blank=True
    )

    def __str__(self):
        return self.username

    @property
    def is_employer(self):
        return hasattr(self, "employer")

    @property
    def is_employee(self):
        return hasattr(self, "contractor")

    @property
    def type(self):
        if self.is_employer:
            return "کارفرما"
        elif self.is_employee:
            return "پیمانکار"
        else:
            return "ناشناس"
