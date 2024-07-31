# import requests

# url = 'http://127.0.0.1:8000/auth/logout/'

# TOKEN = 'fc2da8cf3a4e3aa4bf1b102b0dd2e1ec4f84be51'
# headers = {
#     'Authorization': f'Token {TOKEN}'
# }


# response = requests.delete(url,headers=headers)

# print(response.json())

# test_api/test_logout.py

# import pytest
# from django.urls import reverse
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient

# UserAuth = get_user_model()

# @pytest.mark.django_db
# def test_user_logout(client):

#     client = APIClient()
#     user = UserAuth.objects.create_user(
#         email='aromal123@example.com',
#         password='testpassword',
#         first_name='Test',
#         last_name='User',
#         is_staff=True
#     )


#     refresh = RefreshToken.for_user(user)
#     access_token = str(refresh.access_token)
#     refresh_token = str(refresh)

#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

#     logout_url = reverse('user_auth:user_logout')
#     response = client.delete(logout_url, data={'refresh': refresh_token}, content_type='application/json')

#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['message'] == 'Logout Successfully'

# @pytest.mark.django_db
# def test_user_logout_without_token(client):
#     logout_url = reverse('user_auth:user_logout')
#     response = client.delete(logout_url, data={}, content_type='application/json')

#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#     assert response.data['error'] == 'refresh token is required'

# @pytest.mark.django_db
# def test_user_logout_with_invalid_token(client):
#     user = UserAuth.objects.create_user(
#         email='testuser@example.com',
#         password='testpassword',
#         first_name='Test',
#         last_name='User',
#         is_staff=True
#     )

#     refresh = RefreshToken.for_user(user)
#     access_token = str(refresh.access_token)
    
#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

#     invalid_refresh_token = 'invalid_refresh_token'
#     logout_url = reverse('user_auth:user_logout')
#     response = client.delete(logout_url, data={'refresh': invalid_refresh_token}, content_type='application/json')

#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#     assert 'error' in response.data


