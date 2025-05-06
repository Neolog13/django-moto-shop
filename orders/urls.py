"""
URL configuration for the 'orders' application.

Includes route for creating an order from the cart.
"""


from django.urls import path

from orders import views


app_name = 'orders'


urlpatterns = [
    path('create_order/', views.CreateOrderView.as_view(), name='create_order')
]
