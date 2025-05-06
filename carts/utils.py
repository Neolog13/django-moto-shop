from carts.models import Cart


def get_user_carts(request):
    """
    Retrieve cart items for the current user or anonymous session.

    If the user is authenticated, returns all cart items associated with the user.
    If the user is anonymous, ensures a session key exists and returns cart items
    associated with the session.

    Args:
        request (HttpRequest): The HTTP request object containing user and session information.

    Returns:
        QuerySet: A queryset of Cart objects with related product data prefetched.
    """
        
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')
    
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')
