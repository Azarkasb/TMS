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
    def is_employer(self) -> bool:
        return hasattr(self, "employer")

    @property
    def is_contractor(self) -> bool:
        return hasattr(self, "contractor")

    @property
    def type(self) -> str:
        if self.is_employer:
            return "کارفرما"
        elif self.is_contractor:
            return "پیمانکار"
        else:
            return "ناشناس"
