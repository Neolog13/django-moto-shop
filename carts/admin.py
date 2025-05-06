from django.contrib import admin

from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    """
    Tabular inline admin interface for the Cart model.
    Useful when displaying related cart items within another model’s admin interface
    (e.g., User or Product).
    """
    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Cart entries.
    Provides filtering, searching, and readable display of anonymous users and product names.
    """
    list_display = ["user_display", "product_display", "quantity", "created_timestamp"]
    list_filter = ["created_timestamp", "user", "product__name"]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Anonymous user"
    
    def product_display(self, obj):
        return str(obj.product.name)
