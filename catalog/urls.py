from django.urls import path


from catalog import views



app_name = 'catalog'



urlpatterns = [
    # path('', views.CategoriesView.as_view(), name='index'),
    path('', views.CatalogView.as_view(), name='index'),
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='category'),
    path('product/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
    path('search/', views.CatalogView.as_view(), name='search'),
]
