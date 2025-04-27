from rest_framework import viewsets

from api_v1.serializers import ProductsSerializer
from catalog.models import Products



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


