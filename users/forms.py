from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        return email


class ProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()



class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
