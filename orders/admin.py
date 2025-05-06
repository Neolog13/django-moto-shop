from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):
    """
    Inline admin interface for displaying OrderItem instances within an Order.
    """
    model = OrderItem
    fields = (
        "product",
        "name",
        "price",
        "quantity"
    )
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin interface for individual OrderItem entries.
    """
    list_display = (
        "order",
        "product",
        "name",
        "price",
        "quantity"
    )
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabularAdmin(admin.TabularInline):
    """
    Inline admin interface for displaying Order instances within another related model.
    """
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for customer orders.
    Displays order metadata and associated order items.
    """
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
    )
    inlines = (OrderItemTabularAdmin,)
    