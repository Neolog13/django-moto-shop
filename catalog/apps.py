from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """
    Configuration class for the 'catalog' app.

    Sets the default auto field and registers the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
