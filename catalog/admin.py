from django.contrib import admin

from catalog.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price']
    list_editable = ['price']
    search_fields = ['name', 'description']
    list_filter = ['category']
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        "price"
    ]
