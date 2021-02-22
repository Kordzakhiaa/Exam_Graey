from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q, Sum, Count
from django.shortcuts import render, redirect

from .get_date import date
from .forms import OrderForm
from .models import *


@login_required(login_url='user:login_page')
def order_list(request):
    orders = Order.objects.filter(user_id=request.user.id)
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

    context = {'orders': page,
               'next_page_url': next_url,
               'prev_page_url': prev_url
               }
    return render(request, 'ecommerce/order_list.html', context)


@login_required(login_url='user:login_page')
def home(request):
    concrete_user_order = Order.objects.filter(user_id=request.user.id)
    today = datetime.today()

    context = {
        'concrete_user_order': concrete_user_order,
        'last_week_spend_money': concrete_user_order.filter(created_date__range=[date(7), today]).aggregate(
            spend_money=Sum('price')).get(
            'spend_money'),
        'quantity_of_tickets_last_week': concrete_user_order.filter(created_date__range=[date(7), today]).aggregate(
            quantity_of_tickets=Count('ticket')).get(
            'quantity_of_tickets'),

        'last_month_spend_money': concrete_user_order.filter(created_date__range=[date(30), today]).aggregate(
            spend_money=Sum('price')).get(
            'spend_money'),
        'quantity_of_tickets_last_month': concrete_user_order.filter(created_date__range=[date(7), today]).aggregate(
            quantity_of_tickets=Count('ticket')).get(
            'quantity_of_tickets'),

        'last_year_spend_money': concrete_user_order.filter(created_date__range=[date(365), today]).aggregate(
            spend_money=Sum('price')).get(
            'spend_money'),
        'quantity_of_tickets_last_year': concrete_user_order.filter(created_date__range=[date(7), today]).aggregate(
            quantity_of_tickets=Count('ticket')).get(
            'quantity_of_tickets'),
    }

    return render(request, 'ecommerce/home.html', context)


@login_required(login_url='user:login_page')
def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order_form: Order = form.save(commit=False)
            order_form.user_id = request.user.id
            order_form.save()
            ticket = Ticket.objects.get(id=order_form.ticket.id)
            print('Ticket : ', ticket)
            ticket.status = ticket.UNAVAILABLE
            print('Status : ', ticket.status)
            # ticket = Ticket.objects.filter(status=ticket.AVAILABLE)
            ticket.save()
            return redirect('ecommerce:order_list')

    return render(request, 'ecommerce/order_form.html', {'form': form})
