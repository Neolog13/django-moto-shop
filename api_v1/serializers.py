from rest_framework import serializers

from catalog.models import Product


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("name", "slug", "description", "image", "price", "quantity", "category")