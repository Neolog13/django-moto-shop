from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView
import logging

from main.forms import ContactForm


logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "The Best Motorcycles From The Best Store"
        context['content'] = "FIND YOUR BIKE"
        return context
    

class ContactView(FormView):
    template_name = 'main/contact_form.html'
    form_class = ContactForm
    # success_url = reverse('')

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            if self.request.user.first_name:
                initial['first_name'] = self.request.user.first_name
            else:
                initial['first_name'] = ''
            if self.request.user.email:
                initial['email'] = self.request.user.email
            else:
                initial['email'] = ''
        return initial

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # logger.debug(f"Message from {name} ({email}): {message}")

        return super().form_valid(form)

