from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_OPTIONS = (
    ('D', 'Debit Card'),
    ('P', 'PayPal'),
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=True, widget=forms.TextInput(attrs={
        
        'class': 'form-control',
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    country = CountryField(blank_label='(Select Country)').formfield(
        widget=CountrySelectWidget(
            attrs={
                'class': 'custom-select d-block w-100',
                'placeholder': '123456',
        })
    )
    zipcode = forms.CharField(max_length=6, widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_OPTIONS, required=True)
