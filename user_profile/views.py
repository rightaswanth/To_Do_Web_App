from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from user_auth.models import UserAuth
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



# Create your views here.

@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def user_details(request):

    if request.method == 'GET':

        user_id = request.query_params.get('id')
        if not user_id:
            return Response({"error": "ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserAuth.objects.get(pk=user_id)
        serializer = UserSerializer(user, many=False) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        user_id = request.query_params.get('id')
        if not user_id:
            return Response({"error": "ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserAuth.objects.get(pk=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




