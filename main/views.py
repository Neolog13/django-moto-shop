import logging
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView

from main.forms import ContactForm


logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    """
    Displays the homepage with.
    """
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "The Best Motorcycles From The Best Store"
        context['content'] = "FIND YOUR BIKE"
        return context
    

class ContactView(FormView):
    """
    Renders and processes a contact form.

    If the user is authenticated, pre-fills name and email fields.
    Logs the message and sends an email upon valid form submission.
    """
    template_name = 'main/contact_form.html'
    form_class = ContactForm
    # success_url = reverse_lazy('main:contact')

    def get_success_url(self):
        return reverse("main:contact") + "?success=1"

    def get_initial(self):
        """
        Prefills form with user's name and email if authenticated.
        """
        initial = super().get_initial()
        user = self.request.user

        if user.is_authenticated:
            initial['first_name'] = getattr(user, 'first_name', '')
            initial['email'] = getattr(user, 'email', '')

        return initial

    def form_valid(self, form):
        """
        Handles successful form submission: logs and sends an email.
        """
        first_name = form.cleaned_data['first_name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Log the contact message
        logger.info("Contact form submitted by %s <%s>: %s", first_name, email, message)

        # Send email
        send_mail(
            subject=f"New Contact Message from {first_name}",
            message=message,
            from_email=email,
            recipient_list=['neologfly@gmail.com'],
            fail_silently=False
        )
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        """
        Logs an error when the contact form is submitted with invalid data.
        """
        logger.error("Failed to submit contact form due to invalid data: %s", form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        """
        Adds title to the context for display in the template.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact"
        context["success"] = self.request.GET.get("success") == "1"
        return context
        