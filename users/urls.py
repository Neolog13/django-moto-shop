from django.urls import path, reverse_lazy

from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from users import views

app_name = 'users'

urlpatterns = [
    # Login view for users
    path('login/', views.UserLoginView.as_view(), name='login'),

    # User registration view
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),

    # User profile view
    path('profile/', views.UserProfileView.as_view(), name='profile'),

    # View to show the user's cart
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),

    # Logout view that redirects to main page after logout
    path('logout/', LogoutView.as_view(next_page='main:index'), name='logout'),

    # Password reset views
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name = "users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done")
        ),
        name='password_reset'),

    path('password-reset/done/',
        PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"),
        name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    template_name="users/password_reset_confirm.html",
    success_url=reverse_lazy("users:password_reset_complete")
    ),
    name='password_reset_confirm'),

    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),

    # Password change views
    path('password-change/', views.UserPasswordChange.as_view(), name="password_change"),

    path ('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name='password_change_done'),
]
