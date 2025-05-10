from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from carts.mixins import CartMixin
from carts.services.cart_services import (
    add_product_to_cart,
    remove_product_from_cart,
    update_cart_item_quantity,
)
from catalog.models import Products


class CartAddView(CartMixin, View):
    """
    Add a product to the cart.

    If the product is already in the cart, the quantity is increased.
    If the product is not in the cart, a new cart item is created.
    """

    def post(self, request):
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Products, id=product_id)

        add_product_to_cart(
            user=request.user if request.user.is_authenticated else None,
            session_key=(
                request.session.session_key
                if not request.user.is_authenticated
                else None
            ),
            product=product,
        )

        response_data = {
            "message": "Item added to cart",
            "cart_items_html": self.render_cart(request),
        }
        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
    """
    Change the quantity of a product in the cart
    """

    def post(self, request):
        cart_id = request.POST.get("cart_id")
        new_quantity = int(request.POST.get("quantity", 1))

        try:
            # Use the service to update the quantity
            update_cart_item_quantity(cart_id=cart_id, new_quantity=new_quantity)

            response_data = {
                "message": "Quantity updated",
                "quantity": new_quantity,
                "cart_items_html": self.render_cart(request),
            }

        except ValueError as e:
            response_data = {"message": str(e)}
            return JsonResponse(response_data, status=400)

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):
    """
    Remove a product from the cart
    """

    def post(self, request):
        cart_id = request.POST.get("cart_id")

        try:
            # Use the service to remove the product
            remove_product_from_cart(cart_id)

            response_data = {
                "message": "Product removed from the cart",
                "cart_items_html": self.render_cart(request),
            }

        except ObjectDoesNotExist:
            response_data = {"message": "Cart item not found"}
            return JsonResponse(response_data, status=404)

        return JsonResponse(response_data)
