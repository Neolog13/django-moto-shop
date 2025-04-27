from rest_framework import serializers

from catalog.models import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ("name", "slug", "description", "image", "price", "quantity", "category")