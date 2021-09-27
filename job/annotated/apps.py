from django.apps import AppConfig


class AnnotatedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annotated'
