from rest_framework import serializers
from user_auth.models import User

from rest_framework import status

# class UserLoginSerializer(serializers.Serializer):

#     class Meta:
#         model = User
#         fields = ['id','hash_password','username']


class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','hash_password','username']
        extra_kwargs = {
            'hash_password':{'write_only':True}
        }

class ForgotPasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','hash_password']
        extra_kwargs = {
            'hash_password':{'write_only':True}
        }
    






