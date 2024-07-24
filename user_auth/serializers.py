from rest_framework import serializers
from user_auth.models import UserAuth

from rest_framework import status

class UserLoginSerializer(serializers.Serializer):

    class Meta:
        model = UserAuth
        fields = ['id','password','email']


class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAuth
        fields = ['id','first_name','last_name','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

class ForgotPasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAuth
        fields = ['id','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    






