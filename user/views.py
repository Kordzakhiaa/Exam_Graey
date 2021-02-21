from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from user.forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login_page')

    context = {'form': form}
    return render(request, 'user/register.html', context)


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('ecommerce:home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'user/login.html')


def logout_page(request):
    logout(request)
    return redirect('user:login_page')
