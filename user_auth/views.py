from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from user_auth.serializers import UserRegisterSerializer,LoginSerializer
from rest_framework.exceptions import ValidationError
from .models import UserAuth
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from .exceptions import InvalidEmailException
import re
from django.contrib.auth.hashers import make_password

class UserLogin(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            user = UserAuth.objects.get(email=request.data['email'])
    
            valid = authenticate(request, email=request.data['email'], password=request.data['password'])
            print(valid)
            if valid != None:
                refresh = RefreshToken.for_user(user)
                response = {
                    'data':{
                        'id':user.id,
                        'first_name':user.id,
                        'last_name':user.last_name,
                        'email':user.email,
                        'role_user':user.is_staff
                    },
                    "tokens":{
                        "refresh":str(refresh),
                        "access_token":str(refresh.access_token)
                    },
                    "message":"Login Succesfully",
                    "status_code":200
                }
                return Response(response, status=200)
            return Response({'message': 'password or username is invalid','status_code':401}, status=status.HTTP_401_UNAUTHORIZED)
        except UserAuth.DoesNotExist:
            return Response({'message': 'Invalid User','status_code':404}, status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            return Response({'message':f"{str(e)} is not provided" ,'status_code':401},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'message':str(e),'status_code':404},status=status.HTTP_404_NOT_FOUND)
        
            
class UserRegister(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        
        try:

            if request.data['password'] != request.data['confirm_password']:
                raise ValidationError({'message':'Both Password not same. Must be same'})
            
            if not re.match(r"[^@]+@[^@]+\.[^@]+", request.data['email']):
                raise InvalidEmailException({'message':'Provided email is invalid'})
            
            serializer = UserRegisterSerializer(data = request.data)

            if serializer.is_valid():
                # validated_data = serializer.validated_data
                serializer.validated_data['password'] = make_password(
                    serializer.validated_data['password']
                    )
                user = UserAuth.objects.create(**serializer.validated_data)
                response = {
                    "data":{
                        'first_name':request.data['first_name'],
                        'last_name':request.data['last_name'],
                        'email':request.data['email']
                },
                "message":"Register Succesfully",
                'status_code':201
            }
                return Response(response,status=201)
            return Response(serializer.errors, status=400)
        except InvalidEmailException as e:
            return Response({'message':str(e)},status=e.status_code)
        except ValidationError as e:
            return Response({'messsage':str(e)},status=400)
        except Exception as e:
            return Response({'message':str(e)},status=400)

class PasswordForgot(APIView):

    permission_classes =  [AllowAny]

    def post(self,request,*args,**kwargs):
    
        try:
            user = UserAuth.objects.get(email=request.data['email'])
            refresh = RefreshToken.for_user(user)
            response = {
                'message': "A password reset link has been sent to your email address.",
                'status_code':200,
                'tokens':{
                    'refresh':str(refresh),
                    'access_token':str(refresh.access_token)
                }
            }
            return Response(response,status=200)
        except UserAuth.DoesNotExist:
            return Response({'message':'Invalid User'},status=404)
        
class ResetPassword(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self,request,*args,**kwargs):

        if request.data['password'] != request.data['confirm_password']:
            response = {
                'status':'Unsuccessfull',
                'message':'The password is not same'
            }
            return Response(response,status=400)
        user = request.user
        print(request.user)
        print(user)
        if user:
            user.set_password(request.data['password'])
            user.save()
            return Response({'message':'password reseted','status_code':200},status=200)
        return Response({'message':'Invalid Input'},status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args):
        try:
            print(request.data.get('refresh'))
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({"message":'error','error':'refresh token is required','status_code':400},status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()
            return Response({"message":"Logout Successfully",'status_code':200},status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({"error":str(e),'status_code':400},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e),'status_code':400},status=status.HTTP_400_BAD_REQUEST)  
        