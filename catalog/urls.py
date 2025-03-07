from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_categories, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('category/<slug:category_slug>/', views.catalog_products, name='category'),
    path('search/', views.catalog_products, name='search'),
    # path('category/<slug:category_slug>/<int:page>', views.catalog_products, name='category'),
]
