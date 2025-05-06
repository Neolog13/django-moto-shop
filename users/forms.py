from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

from users.models import User


User = get_user_model()

class UserLoginForm(AuthenticationForm):
    """
    Form for user login using Django's built-in authentication system.
    """
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    """
    Custom user registration form extending Django's UserCreationForm.
    Ensures email uniqueness.
    """
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        """
        Check if email already exists in the database.
        """
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        return email


class ProfileForm(UserChangeForm):
    """
    User profile update form.
    """
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )


class UserPasswordChangeForm(PasswordChangeForm):
    """
    Form for changing user password with custom widget styling.
    """
    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    new_password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
        )
