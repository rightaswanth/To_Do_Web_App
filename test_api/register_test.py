# import requests

# url = 'http://127.0.0.1:8000/auth/register/'

# user_data = {
#     "first_name": "akshay",
#     "last_name": "A K",
#     "email": "akshay@example.com",
#     "password": "SecureP@ssw0rd",
#     "confirm_password":"SecureP@ssw0rd"
# }

# response = requests.post(url,json=user_data)

# print(response.json())

import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_register_successful(client):

    register_url = reverse('user_auth:user_register')

    response = client.post(register_url, {
        'first_name': 'nima',
        'last_name': 'kk',
        'email': 'nima.kk123@example.com',
        'password': 'SecureP@ssw0rd12345',
        'confirm_password': 'SecureP@ssw0rd12345'
    })

    print(response.data) 
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_register_password_mismatch(client):

    register_url = reverse('user_auth:user_register')

    response = client.post(register_url, {
        'first_name': 'nima',
        'last_name': 'kk',
        'email': 'nima.kk123@example.com',
        'password': 'SecureP@ssw0rd123',
        'confirm_password': 'SecureP@ssw0rd12345'
    })

    print(response.data) 
    assert response.status_code == 400


@pytest.mark.django_db
def test_register_data_missing(client):
    """
    1 st case : data is null
    2 end case : data is missing
    3 rd email format in not correct
    """

    register_url = reverse('user_auth:user_register')

    response = client.post(register_url, {
        'first_name': 'nima',
        'last_name': 'kk',
        'email': 'nimakk123examplecom',
        'password': 'SecureP@ssw0rd123',
        'confirm_password': 'SecureP@ssw0rd123'
    })

    print(response.data) 
    assert response.status_code == 400







