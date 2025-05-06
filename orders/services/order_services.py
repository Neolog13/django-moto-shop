from django.forms import ValidationError
from orders.models import Order, OrderItem


def create_order_from_cart(cart_items, form, user):
    """
    Creates an order from the user's cart items.

    This function handles the creation of the order, checks for stock availability,
    creates the order items, and updates product quantities accordingly.

    Args:
        cart_items (QuerySet): The user's cart items.
        form (CreateOrderForm): The form with the order data.
        user (User): The authenticated user placing the order.

    Returns:
        Order: The created Order object or None if there was an issue.
    """
    order = Order.objects.create(
        user=user,
        phone_number=form.cleaned_data['phone_number'],
        requires_delivery=form.cleaned_data['requires_delivery'],
        delivery_address=form.cleaned_data['delivery_address'],
        payment_on_get=form.cleaned_data['payment_on_get'],
    )

    for cart_item in cart_items:
        product = cart_item.product
        name = product.name
        price = product.sell_price()
        quantity = cart_item.quantity

        if product.quantity < quantity:
            raise ValidationError(f'Insufficient stock for {name}. Available stock: {product.quantity}')

        OrderItem.objects.create(
            order=order,
            product=product,
            name=name,
            price=price,
            quantity=quantity,
        )

        product.quantity -= quantity
        product.save()

    # Clear the cart items after order is placed
    cart_items.delete()

    return order