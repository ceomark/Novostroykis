from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager


# Расширенная модель пользователя
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrator'),
        ('user', 'User'),
        ('moderator', 'Moderator'),
    )

    email = models.EmailField(unique=True)  # Используем email как уникальный идентификатор
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)  # Поле для подтверждения email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # Создание групп при создании пользователя (опционально)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user_type == 'moderator':
            group, created = Group.objects.get_or_create(name='Moderators')
            self.groups.add(group)
        elif self.user_type == 'admin':
            group, created = Group.objects.get_or_create(name='Administrators')
            self.groups.add(group)


# Профиль пользователя
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    saved_searches = models.JSONField(default=list, blank=True)
    favorite_properties = models.ManyToManyField('properties.Property', blank=True, related_name='favorited_by')

    def __str__(self):
        return f"{self.user.email}'s profile"


# Функция для создания пользовательских групп
def create_user_groups():
    # Создание группы модераторов
    moderator_group, created = Group.objects.get_or_create(name='Moderators')
    admin_group, created = Group.objects.get_or_create(name='Administrators')

    # Добавление стандартных разрешений
    permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
    moderator_group.permissions.set(permissions)
    admin_group.permissions.set(permissions)


# Функции проверки доступа (для использования в представлениях)
def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Administrators').exists()


def is_moderator(user):
    return user.is_authenticated and user.groups.filter(name='Moderators').exists()


class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False)