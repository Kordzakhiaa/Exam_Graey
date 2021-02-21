from django import forms

from ecommerce.models import Order, Ticket


class OrderForm(forms.ModelForm):
    # ticket =
    order_start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    order_end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = [
            'ticket',
            'order_start_date',
            'order_end_date'
        ]
