from carts.models import Cart


# Returns carts for authenticated users or based on session key for guests
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')
    
    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')

# Проверить на работоспособность и изменить первичный код если все ок
# def get_user_carts(request):
#     # Создаем session_key для анонимных пользователей, если его нет
#     if not request.session.session_key:
#         request.session.create()

#     # Определяем фильтрацию на основе того, аутентифицирован ли пользователь
#     filter_condition = {'user': request.user} if request.user.is_authenticated else {'session_key': request.session.session_key}

#     # Возвращаем корзины с предзагруженными продуктами
#     return Cart.objects.filter(**filter_condition).select_related('product')