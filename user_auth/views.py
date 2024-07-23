from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from user_auth.serializers import UserRegisterSerializer, ForgotPasswordSerializer
from rest_framework.exceptions import ValidationError 
from .models import User
# Create your views here.

class UserLogin(APIView):
    def post(self,request,*args,**kwargs):
        
        if User.objects.filter(username=request.data['username']).exists():
            user = User.objects.get(username=request.data['username'])
            if user.hash_password == request.data['password']:
                response = {
                    'Success':True,
                    'username':user.username,
                    'status':202
                }
                return JsonResponse(response,status=status.HTTP_202_ACCEPTED)
            return JsonResponse({'message':'Incorrect Password'},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Invalid User'},status=status.HTTP_404_NOT_FOUND)
    
class UserRegister(APIView):
    def post(self,request,*args,**kwargs):

        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if password != confirm_password:
            raise ValidationError({'message':'Both Password not same. Must be same'})
        data = dict(request.data)
        data.pop('confirm_password',None)
        if 'password' in data:
            data['hash_password'] = data.pop('password')
        for key, value in data.items():
            if isinstance(value, list) and len(value) == 1:
                data[key] = value[0]
        user_name = data['first_name'] + data['last_name']
        data['username'] = user_name.strip()
        # print(data['hash_password'])
        serializer = UserRegisterSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'status':200,
                'username': data['username'],
                'message':'new user created'
            }
            return JsonResponse(response,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordForgot(APIView):
    def post(self,request,*args,**kwargs):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            response = {
                'Succes':True,
                'message': "Reset Password mail is sended to the email"
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response({'message':'The user is not existing'},status=status.HTTP_404_NOT_FOUND)

class ResetPassword(APIView):

    def patch(self,request,*args,**kwargs):

        if request.data['password'] != request.data['confirm_password']:
            response = {
                'status':'Unsuccessfull',
                'message':'The password is not same'
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        data = dict(request.data)
        data.pop('confirm_password',None)
        if 'password' in data:
            data['hashed_password'] = data.pop('password')
        data['hashed_password'] = data['hashed_password'][0]
        serializer = ForgotPasswordSerializer(data=data)

        if serializer.is_valid():
            response = {
                'message':'Password reseted'
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response({'message':'Invalid Input'},status=status.HTTP_400_BAD_REQUEST)


        
        

class UserLogout(APIView):
    pass
