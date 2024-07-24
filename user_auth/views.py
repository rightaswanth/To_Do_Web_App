from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from user_auth.serializers import UserRegisterSerializer, ForgotPasswordSerializer, UserLoginSerializer
from rest_framework.exceptions import ValidationError 
from .models import UserAuth
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny


class UserLogin(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        for key, value in data.items():
            if isinstance(value, list) and len(value) == 1:
                data[key] = value[0]
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            email = data.get('email')
            password = data.get('password')

            try:
                user = UserAuth.objects.get(email=email)
            except UserAuth.DoesNotExist:
                return Response({'message': 'Invalid User'}, status=status.HTTP_404_NOT_FOUND)

            if user.password == password:
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'Success': True,
                    'username': user.email,
                    'token': token.key,
                    'status': 202
                }
                return Response(response, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Incorrect Password'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegister(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request,*args,**kwargs):
        
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if password != confirm_password:
            raise ValidationError({'message':'Both Password not same. Must be same'})
        data = dict(request.data)
        data.pop('confirm_password',None)

        for key, value in data.items():
            if isinstance(value, list) and len(value) == 1:
                data[key] = value[0]
        
        serializer = UserRegisterSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'status':200,
                'username': data['email'],
                'message':'new user created'
            }
            return JsonResponse(response,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordForgot(APIView):

    permission_classes =  [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        email = request.data['email']
        if UserAuth.objects.filter(email=email).exists():
            response = {
                'Succes':True,
                'message': "Reset Password mail is sended to the email id"
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response({'message':'The user is not existing'},status=status.HTTP_404_NOT_FOUND)

class ResetPassword(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self,request,*args,**kwargs):

        if request.data['password'] != request.data['confirm_password']:
            response = {
                'status':'Unsuccessfull',
                'message':'The password is not same'
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        data = dict(request.data)
        data.pop('confirm_password',None)
        data['password'] = data['password'][0]
        password = data['password']
        if UserAuth.objects.filter(email=request.user).exists():
            UserAuth.objects.filter(email=request.user).update(password=password)
            return Response({'message':'password reseted'})
        return Response({'message':'Invalid Input'},status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'message':'Log Out.....'}, status=status.HTTP_200_OK)
