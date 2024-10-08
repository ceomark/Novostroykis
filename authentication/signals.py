from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.apps import AppConfig
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, UserProfile  # Импорт модели User

# Создание групп пользователей после каждой миграции
@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Создание группы модераторов
    moderator_group, created = Group.objects.get_or_create(name='Moderators')
    admin_group, created = Group.objects.get_or_create(name='Administrators')

    # Добавление стандартных разрешений
    permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
    moderator_group.permissions.set(permissions)
    admin_group.permissions.set(permissions)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)