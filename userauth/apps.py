from django.apps import AppConfig


class AuthorizationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userauth'

    def ready(self):
        import userauth.signals