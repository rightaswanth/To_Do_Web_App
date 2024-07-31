from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from task.serializers import TaskSerializer
from task.models import Task
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter

# Create your views here.

class ListCreateTask(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = TaskFilter
    ordering_fields = ['created_at', 'due_date']
    ordering = ['created_at']
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}
    
    def list(self, request, *args, **kwargs):
        print(request.query_params)
        result = super().list(request, *args, **kwargs)
        response = {
            "data":result.data,
            "status_code":200,
        }
        return Response(response,status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        result = super().create(request, *args, **kwargs)
        response = {
            "data":result.data,
            "status_code":200,
        }
        return Response(response,status=status.HTTP_200_OK) 

        
    
class UpdateDeleteItem(mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def put(self, request, *args, **kwargs):
        try:
            task = Task.objects.get(pk=self.kwargs.get('pk'))
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(task)
        result = self.update(request, *args, **kwargs)
        response = {"data":serializer.data,"message":'Task updated',
                         'status_code':result.status_code}
        return Response(response,status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        
        try:
            task = Task.objects.get(pk=self.kwargs.get('pk'))
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(task)
        response = self.partial_update(request, *args, **kwargs)
        return Response({"data":serializer.data,'message':'Partially Updated','status_code':response.status_code},status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, *kwargs)
        return Response({'message':'Task Deleted',
                        'status_code':response.status_code}, status=status.HTTP_204_NO_CONTENT)
    




    
