from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrator'),
        ('user', 'User'),
        ('moderator', 'Moderator'),
    )

    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)  # Пользователь может входить в систему
    is_email_verified = models.BooleanField(default=False)  # Email подтвержден или нет

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    saved_searches = models.JSONField(default=list, blank=True)
    favorite_properties = models.ManyToManyField('properties.Property', blank=True, related_name='favorited_by')

    def __str__(self):
        return f"{self.user.email}'s profile"