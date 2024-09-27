from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        # Импортируем сигналы при готовности приложения
        import authentication.signals
