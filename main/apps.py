from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    Configuration for the 'main' app.

    This class is used to configure the 'main' Django application.
    It defines the default auto field type and the name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
