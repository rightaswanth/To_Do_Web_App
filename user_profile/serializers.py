from rest_framework import serializers
from user_auth.models import UserAuth

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAuth
        fields = ['first_name','last_name','email']
        