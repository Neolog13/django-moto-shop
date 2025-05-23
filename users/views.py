from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from requests import session

from carts.models import Cart
from common.mixins import CacheMixin
from orders.models import Order, OrderItem
from users.forms import (
    ProfileForm,
    UserLoginForm,
    UserPasswordChangeForm,
    UserRegistrationForm
)


class UserLoginView(LoginView):
    """
    View for handling user login.
    Authenticates the user, assigns carts from session, and displays success message.
    """
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('main:index')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key

        user = form.get_user()

        if user:
            auth.login(self.request, user)
            if session_key:
                # delete old authorized user carts
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                #add new authorized user carts from anonimous session
                Cart.objects.filter(session_key=session_key).update(user=user)

                messages.success(self.request, "You are logged in")

                return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Authorization'
        return context


class UserRegistrationView(CreateView):
    """
    View for handling user registration.
    Registers a new user, logs them in, assigns carts, and displays success message.
    """
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')


    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)


        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, 'You have successfully registered and logged into your account')
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context


class UserProfileView(LoginRequiredMixin, CacheMixin, UpdateView):
    """
    View for displaying and updating user profile.
    Also shows the user's order history with related items.
    """
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "An error has occurred")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'

        orders =  Order.objects.filter(user=self.request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")


        context['orders'] = self.set_get_cache(orders, f"user_{self.request.user.id}_orders", 60 * 2)
        return context


class UserCartView(TemplateView):
    """
    View for displaying the user's cart.
    """
    template_name = 'users/users_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cart'
        return context


class UserPasswordChange(PasswordChangeView):
    """
    View for allowing the user to change their password.
    """
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Change password"}
