from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    name = models.CharField(max_length=200, unique=True)
    start_date = models.DateTimeField(verbose_name=_("Start Date"))
    end_date = models.DateTimeField(verbose_name=_("End Date"))
    code = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(to='user.User', on_delete=models.SET_NULL, null=True, related_name=_('Orders'))
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name=_('Orders'))
    created_date = models.DateTimeField(auto_now=True, verbose_name=_("Created Date"))

    def __str__(self):
        return f"{self.user}'s order"
