from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form__input', 'placeholder': 'E-mail'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': 'Your text'}), required=True)
