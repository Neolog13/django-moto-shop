import re

from django import forms


class CreateOrderForm(forms.Form):
    """
    Form for creating a new order.

    Includes customer details, delivery options, and payment preferences.
    Validates phone number to ensure correct format.
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
            ],
        )

    def clean_phone_number(self):
        """
        Validates that the phone number contains only digits and is exactly 10 digits long.
        """
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Phone number must contain only digits")
        
        if not re.fullmatch(r"^\d{10}$", data):
            raise forms.ValidationError("Phone number must be exactly 10 digits long.")

        return data
    