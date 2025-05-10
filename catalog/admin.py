from django.contrib import admin
from catalog.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Admin interface customization for Category model.
    Automatically fills slug from the name and displays category name in list view.
    """

    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """
    Admin interface customization for Product model.
    Provides full control over product fields, filtering, inline editing, and search.
    """

    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "price", "quantity", "category"]
    list_editable = ["price", "quantity"]
    search_fields = ["name", "description"]
    list_filter = ["category", "quantity"]
    fields = ["name", "category", "slug", "description", "image", "price", "quantity"]
