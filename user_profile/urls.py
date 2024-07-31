from django.urls import path
from user_profile import views

urlpatterns = [
    path('user/',views.user_details,name='user_details')
]