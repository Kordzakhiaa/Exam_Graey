from django.db import models
from django.utils.translation import ugettext_lazy as _
import random


class Ticket(models.Model):
    # STATUS = [
    #     ('available', 'available'),
    #     ('unavailable', 'unavailable'),
    # ]
    name = models.CharField(max_length=200, unique=True)
    start_date = models.DateTimeField(verbose_name=_("Start Date"))
    end_date = models.DateTimeField(verbose_name=_("End Date"))
    code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # status = models.CharField(max_length=50, choices=STATUS, default='available')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = str(random.random())[2:-1]
        super(Ticket, self).save(*args, *kwargs)


class Order(models.Model):
    user = models.ForeignKey(to='user.User', on_delete=models.SET_NULL, null=True, related_name=_('Orders'))
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name=_('Orders'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Price"), default=None)

    def __str__(self):
        return f"{self.user.email}'s order"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.ticket.price
        super(Order, self).save(*args, **kwargs)
