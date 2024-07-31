# import pytest
# from django.urls import reverse
# from rest_framework.test import APIClient
# from rest_framework import status
# from task.models import Task, UserAuth
# from task.serializers import TaskSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# import uuid

# @pytest.fixture
# def api_client():
#     return APIClient()

# @pytest.fixture
# def create_user():
#     user = UserAuth.objects.create_user(
#         email=f'testuser_{uuid.uuid4()}@example.com',
#         password='testpassword',
#         first_name='Test',
#         last_name='User',
#         is_staff=True
#     )
#     return user

# @pytest.fixture
# def create_tasks(create_user):
#     user = create_user
#     Task.objects.create(
#         title='Task 1',
#         description='Task 1 description',
#         user=user,
#         priority=0,
#         current_status=0
#     )
#     Task.objects.create(
#         title='Task 2',
#         description='Task 2 description',
#         user=user,
#         priority=1,
#         current_status=1
#     )

# @pytest.mark.django_db
# def test_list_tasks(api_client, create_user, create_tasks):
#     user = create_user
#     refresh = RefreshToken.for_user(user)
#     access_token = str(refresh.access_token)

#     api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

#     url = reverse('your_app:list_create_task')
#     response = api_client.get(url)

#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['status_code'] == 200
#     assert len(response.data['data']) == 2  # Ensure it lists the 2 tasks

# @pytest.mark.django_db
# def test_create_task(api_client, create_user):
#     user = create_user
#     refresh = RefreshToken.for_user(user)
#     access_token = str(refresh.access_token)

#     api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

#     url = reverse('your_app:list_create_task')
#     task_data = {
#         "title": "New Task",
#         "description": "New task description",
#         "priority": 0,
#         "current_status": 0
#     }

#     response = api_client.post(url, data=task_data, format='json')

#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['status_code'] == 200
#     assert response.data['data']['title'] == "New Task"
#     assert response.data['data']['description'] == "New task description"
#     assert response.data['data']['priority'] == 0
#     assert response.data['data']['current_status'] == 0
#     assert Task.objects.filter(title="New Task").exists()
