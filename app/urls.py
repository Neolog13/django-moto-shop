"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from app import settings

from main.sitemaps import MotoSitemap, CategoryMotoSitemap 
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'moto': MotoSitemap,
    'cats': CategoryMotoSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("user/", include("users.urls", namespace="user")),
    path("cart/", include("carts.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("social-auth/", include("social_django.urls", namespace='social')),
    path("api/v1/", include("api_v1.urls", namespace="api_v1")),
    path("api/v1/drf-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("sitemap.xml/", sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]


if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
