from django import forms
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=True)
    apartment_address = forms.CharField(required=False)
    country = CountryField(blank_label='(Select Country)')
    zipcode = forms.CharField(max_length=6)

    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput)
    save_info = forms.BooleanField(widget=forms.CheckboxInput)

    payment_option = forms.BooleanField(widget=forms.RadioSelect)
    
