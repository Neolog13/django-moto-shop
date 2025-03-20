from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Name', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    message = forms.CharField(widget=forms.Textarea, label='message', required=True)
