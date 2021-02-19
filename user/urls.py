from django.urls import path
from user.views import register_page, login_page

app_name = 'user'

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
]
