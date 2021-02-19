from django.contrib.auth.decorators import login_required as lr
from django.urls import path
from .views import *

app_name = 'ecommerce'

urlpatterns = [
    path('home/', home, name='home'),
    path('create_order/', create_order, name='create_order'),
    path('order_list/', lr(order_list), name='order_list'),
]
