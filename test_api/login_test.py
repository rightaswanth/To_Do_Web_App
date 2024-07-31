# import requests

# url = 'http://127.0.0.1:8000/auth/login/'

# data = {
#     'email':'john.bosco@example.com',
#     'password': 'SecureP@ssw0rd'
# }

# response = requests.post(url,json=data)

# print(response.json())
import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model

UserAuth = get_user_model()

@pytest.mark.django_db
def test_login_successful(client):

    user = UserAuth.objects.create_user(
        email='akshay.ak123@example.com',
        password='ak@123',
        first_name='Akshay',
        last_name='A K'
    )

    login_url = reverse('user_auth:user_login')
    response = client.post(login_url, {
        'email': 'akshay.ak123@example.com',
        'password': 'ak@123'
    })
    print("/n",response.content)
    print("/n",response.status_code)
    assert response.status_code == status.HTTP_200_OK
    assert 'tokens' in response.data
    assert 'access_token' in response.data['tokens']
    assert 'refresh' in response.data['tokens']
    assert response.data['data']['email'] == 'akshay.ak123@example.com'

@pytest.mark.django_db
def test_login_invalid_user(client):

    """
    1st case : The email is not existing
    2 end case : email is null
    """
    user = UserAuth.objects.create_user(
        email='abhinav.c123@example.com',
        password='ab@123',
        first_name='Abinav',
        last_name='C'
    )


    login_url = reverse('user_auth:user_login')
    response = client.post(login_url, {
        'email': 'abhinav.123@example.com',
        'password': 'ab@123'
    })
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert 'message' in response.data
    
@pytest.mark.django_db
def test_login_incorrect_password(client):

    """
    1st case : password is incorrect
    2 end case : password is null
    """
    user = UserAuth.objects.create_user(
        email='niranjan.vp123@example.com',
        password='nj@123',
        first_name='Niranjan',
        last_name='V P'
    )


    login_url = reverse('user_auth:user_login')
    response = client.post(login_url, {
        'email': 'niranjan.vp123@example.com',
        # 'password': 'nj@12345'
    })
    print(response.data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert 'message' in response.data

