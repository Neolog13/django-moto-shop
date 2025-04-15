from django.urls import path

from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
    path('logout/', LogoutView.as_view(next_page='main:index'), name='logout'),

    path('password-change/', views.UserPasswordChange.as_view(), name="password_change"),
    path ('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name='password_change_done'),
]
