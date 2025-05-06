from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin interface for managing User model instances.
    """
    list_display = ["username", "first_name", "last_name", "email"]
    search_field = ["username", "first_name", "last_name", "email"]

    inlines = [CartTabAdmin, OrderTabularAdmin]
