from django import forms


class ContactForm(forms.Form):
    """
    A form for submitting a contact message.

    This form is designed to collect the user's first name, email address, 
    and message. It includes the necessary validation to ensure that the 
    fields are filled out correctly.
    """
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'Name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form__input',
            'placeholder': 'E-mail'
        })
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form__textarea',
            'placeholder': 'Your text'
        })
    )
