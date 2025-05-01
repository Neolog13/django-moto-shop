from django.contrib.auth import login
from django.contrib import messages

from carts.models import Cart


def login_user_and_assign_cart(request, user):
    login(request, user)
    session_key = request.session.session_key

    if session_key:
        Cart.objects.filter(user=user).delete()
        Cart.objects.filter(session_key=session_key).update(user=user)

    messages.success(request, "You are logged in")