from django.shortcuts import get_object_or_404
from carts.models import Cart


def add_product_to_cart(user, session_key, product, quantity=1):
    """
    Add a product to the cart, or update the quantity if it already exists in the cart.
    """
    cart_item = Cart.objects.filter(product=product, user=user, session_key=session_key).first()

    if cart_item:
        cart_item.quantity += quantity
        cart_item.save()
    else:
        Cart.objects.create(user=user, session_key=session_key, product=product, quantity=quantity)


def update_cart_item_quantity(cart_id, new_quantity):
    """
    Update the quantity of a cart item.
    """
    if new_quantity < 1:
        raise ValueError("Quantity must be at least 1")

    cart_item = Cart.objects.get(id=cart_id)
    cart_item.quantity = new_quantity
    cart_item.save()


def remove_product_from_cart(cart_id):
    """
    Remove a product from the cart.
    """
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()