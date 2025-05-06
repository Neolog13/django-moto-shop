from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.services.order_services import create_order_from_cart


class CreateOrderView(LoginRequiredMixin, FormView):
    """
    View for creating an order from the cart.

    This view allows authenticated users to create an order from the products
    in their cart. If the cart contains products, the order will be processed.
    If there is not enough stock, an error message will be displayed.
    """
    template_name = 'orders/create_order.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('users:profile')

    def get_initial(self):
        """
        Sets initial form data for first name and last name from the user's profile.
        """
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial

    def form_valid(self, form):
        """
        Handles the form submission if it is valid.
        Processes the cart and creates an order.
        If there is insufficient stock, raises a validation error.

        Args:
            form (CreateOrderForm): The valid form with user order data.

        Returns:
            HttpResponse: Redirect to the user's profile on success, or back to the form on failure.
        """
        try:
            # Using a transaction to ensure atomicity
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if not cart_items.exists():
                    messages.error(self.request, 'Your cart is empty.')
                    return redirect('orders:create_order')

                order = create_order_from_cart(cart_items, form, user)

                if order:
                    messages.success(self.request, 'Order placed successfully!')
                    return redirect(self.success_url)
                else:
                    messages.error(self.request, 'There was an error processing your order.')
                    return redirect('orders:create_order')

        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect('orders:create_order')

    def form_invalid(self, form):
        """
        Handles the case when the form is invalid.
        Displays a message prompting the user to fill in all required fields.

        Args:
            form (CreateOrderForm): The invalid form.

        Returns:
            HttpResponse: Redirects the user back to the order creation page.
        """
        messages.error(self.request, 'Please fill in all required fields!')
        return redirect('orders:create_order')

    def get_context_data(self, **kwargs):
        """
        Adds additional context data for the order creation page.

        Args:
            **kwargs: Keyword arguments for context data.

        Returns:
            dict: Updated context with additional data for rendering the page.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Order processing'
        context['order'] = True
        return context
        