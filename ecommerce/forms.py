from django import forms

from ecommerce.models import Order, Ticket


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'ticket',
        ]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['ticket'].queryset = Ticket.objects.filter(status=Ticket.AVAILABLE)
