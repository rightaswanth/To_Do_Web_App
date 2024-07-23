from django.urls import path
from .views import *

urlpatterns = [
    path('login/',UserLogin.as_view(),name='user_login'),
    path('register/',UserRegister.as_view(),name='user_register'),
    path('logout/',UserLogout.as_view(),name='user_logout'),
    path('reset_password/',ResetPassword.as_view(),name='password_reset'),
]