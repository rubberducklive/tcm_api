from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from core.models import PrimaryUUIDTimeStampedModel


class User(AbstractUser, PrimaryUUIDTimeStampedModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
