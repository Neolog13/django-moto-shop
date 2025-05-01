from rest_framework import viewsets

from api_v1.serializers import ProductsSerializer
from catalog.models import Product



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


