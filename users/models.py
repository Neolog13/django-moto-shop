from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Adds an optional profile image and phone number field.
    """
    image = models.ImageField(
        upload_to='users_images',
        blank=True,
        null=True,
        verbose_name='Avatar',
        help_text = 'User profile avatar'
    )
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text = 'User phone number'
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
