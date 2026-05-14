from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, max_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'password', 'role', 'depertment', 'level']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'full_name', 'role', 'role', 'depertment', 'level', 'date_joined']
        read_only = ['id', 'date_joined']
#yooo