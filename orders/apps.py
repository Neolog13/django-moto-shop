from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """
    Configuration class for the 'orders' application.

    This class defines application-specific settings and behaviors for the
    orders app, including the default auto field for models.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
