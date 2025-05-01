from django.urls import path
from catalog import views


app_name = 'catalog'


urlpatterns = [
    # Product category page
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='category'),

    # Individual product detail page
    path('product/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
    
    # Search results page (uses the same view as the catalog)
    path('search/', views.CatalogView.as_view(), name='search'),
]
