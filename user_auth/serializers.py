from rest_framework import serializers
from user_auth.models import UserAuth
from django.contrib.auth.hashers import make_password
from rest_framework import status


class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAuth
        fields = ['id','email','password']

class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAuth
        fields = ['first_name','last_name','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

        # def create(self, validated_data):
        #     validated_data['password'] = make_password(validated_data['password'])
        #     return super(UserRegisterSerializer, self).create(validated_data)




