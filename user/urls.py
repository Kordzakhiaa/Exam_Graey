from django.urls import path
from user.views import register_page, login_page, logout_page

app_name = 'user'

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
]
