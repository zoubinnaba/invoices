from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class UserProfile(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',  # Custom related name to avoid conflict
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',  # Custom related name to avoid conflict
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email