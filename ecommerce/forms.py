from django import forms

from ecommerce.models import Order, Ticket


class OrderForm(forms.ModelForm):
    order_start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    order_end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = [
            'ticket',
            'order_start_date',
            'order_end_date'
        ]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['ticket'].queryset = Ticket.objects.filter(status=Ticket.AVAILABLE)
