from django.template.loader import render_to_string
from django.urls import reverse

from carts.models import Cart
from carts.utils import get_user_carts


class CartMixin:
    """
    A mixin providing helper methods for working with the shopping cart.
    
    Includes methods for retrieving a specific cart item and rendering the cart's HTML.
    """
    def get_cart(self, request, product=None, cart_id=None):
        """
        Retrieve a cart item for the current user or session.

        Args:
            request (HttpRequest): The current request object.
            product (Product, optional): A product to filter the cart item by.
            cart_id (int, optional): An ID to filter the cart item by.

        Returns:
            Cart or None: The first matching cart item, or None if not found.
        """

        if request.user.is_authenticated:
            query_kwargs = {"user": request.user}
        else:
            query_kwargs = {"session_key": request.session.session_key}

        if product:
            query_kwargs["product"] = product
        if cart_id:
            query_kwargs["id"] = cart_id

        return Cart.objects.filter(**query_kwargs).first()

    def render_cart(self, request):
        """
        Render the HTML of the user's cart.

        Args:
            request (HttpRequest): The current request object.

        Returns:
            str: Rendered HTML string of the cart.
        """
        user_cart = get_user_carts(request)
        context = {"carts": user_cart}

        # if referer page is create_order add key orders: True to context
        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context["order"] = True

        return render_to_string(
            "carts/includes/included_cart.html", context, request=request
        )
