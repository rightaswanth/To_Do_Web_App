from django.urls import path
from .views import *

app_name = 'user_auth'

urlpatterns = [
    path('login/',UserLogin.as_view(),name='user_login'),
    path('register/',UserRegister.as_view(),name='user_register'),
    path('logout/',UserLogout.as_view(),name='user_logout'),
    path('reset/',ResetPassword.as_view(),name='password_reset'),
    path('forgot/',PasswordForgot.as_view(),name='forgot_password'),
]