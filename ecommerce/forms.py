from django.forms import ModelForm
from django import forms

from ecommerce.models import Order, Ticket


class OrderForm(ModelForm):
    order_start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    order_end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = '__all__'
