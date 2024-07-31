from django.urls import path
from .views import ListCreateTask,UpdateDeleteItem

urlpatterns = [
    path('task/',ListCreateTask.as_view(),name='task_list_create'),
    path('task/<int:pk>',UpdateDeleteItem.as_view(),name='task_delete_update'),
]