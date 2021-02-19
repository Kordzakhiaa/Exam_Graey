from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(verbose_name=_("Start time"))
    end_date = models.DateTimeField(verbose_name=_("End time"))
    code = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True, verbose_name=_("Created Date"))
    order_start_date = models.DateTimeField(verbose_name=_("Start time"))
    order_end_date = models.DateTimeField(verbose_name=_("End time"))
