from argparse import Namespace
from django.urls import include, path

from rest_framework import routers
from api_v1.views import ProductViewSet


app_name = 'api_v1'


router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)



urlpatterns = [
    path('', include(router.urls)), 
]