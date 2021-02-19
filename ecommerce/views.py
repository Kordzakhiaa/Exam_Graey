from datetime import datetime

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import *


def order_list(request):
    orders = Order.objects.all()
    q = request.GET.get('q')
    if q:
        orders = Order.objects.filter(Q(ticket__name__icontains=q) | Q(ticket__name__icontains=q))
    p = Paginator(orders, 3)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    context = {'orders': orders}
    return render(request, 'ecommerce/order_list.html', context)


def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:order_list')

    return render(request, 'ecommerce/order_form.html', {'form': form})


def washer_detail(request, pk: int):
    orders = CarWasher.objects.get(pk=pk)
    orders = washer_by_id.orders.all()
    today = datetime.today()

    context = {
        'washer_by_id': washer_by_id,
        'today_earned': orders.filter(created_date__range=[date(1), today]).aggregate(salary=Sum('order_price')).get(
            'salary'),
        'weekly_earned': orders.filter(created_date__range=[date(7), today]).aggregate(salary=Sum('order_price')).get(
            'salary'),
        'monthly_earned': orders.filter(created_date__range=[date(30), today]).aggregate(salary=Sum('order_price')).get(
            'salary'),
        'yearly_earned': orders.filter(created_date__range=[date(365), today]).aggregate(salary=Sum('order_price')).get(
            'salary'),
    }
    return render(request, 'washer_details.html', context)



def home(request):
    return render(request, 'ecommerce/home.html')
