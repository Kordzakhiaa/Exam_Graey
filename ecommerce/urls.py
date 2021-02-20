from django.urls import path
from .views import *

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('create_order/', create_order, name='create_order'),
    path('order_list/', order_list, name='order_list'),
]
