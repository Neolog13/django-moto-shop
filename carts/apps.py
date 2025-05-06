from django.apps import AppConfig


class CartsConfig(AppConfig):
    """
    Configuration class for the carts application.

    Sets the default auto field type and provides a human-readable verbose name
    for the Django admin interface.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'
    verbose_name = "Carts"
