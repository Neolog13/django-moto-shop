from django.urls import path
from django.contrib import admin

from main import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact')
]
