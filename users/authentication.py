import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


logger = logging.getLogger(__name__)

class EmailAuthBackend(BaseBackend):
    """
    Custom authentication backend that authenticates users using their email address
    instead of a username.

    This backend allows users to log in with their email address and password, 
    providing an alternative to the default username-based authentication.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate the user using their email address and password.

        Args:
            request: The HTTP request object.
            username (str): The email address provided by the user for authentication.
            password (str): The password provided by the user for authentication.

        Returns:
            User instance if authentication is successful, None otherwise.
        """
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None
        except user_model.DoesNotExist:
            logger.warning("Authentication failed: User with email %s does not exist.", username)
            return None
        except user_model.MultipleObjectsReturned:
            logger.error("Multiple users found with email %s.", username)
            return None

    def get_user(self, user_id):
        """
        Retrieve a user instance by their primary key (user ID).

        Args:
            user_id (int): The primary key of the user to retrieve.

        Returns:
            User instance if found, None otherwise.
        """
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
