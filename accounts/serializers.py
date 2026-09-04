from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['id', 'email', 'full_name', 'password', 'role', 'department', 'level']
=======
        fields = ['id', 'email', 'full_name', 'password', 'faculty', 'department', 'role']
        read_only_fields = ['id', 'date_joined', 'role']
>>>>>>> 5b81de312c97f8c81c31149a7945452743572f2c

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['id', 'full_name', 'role', 'role', 'department', 'level', 'date_joined']
        read_only = ['id', 'date_joined']
=======
        fields = ['id', 'full_name', 'role', 'faculty', 'department', 'date_joined']
        read_only_fields = ['id', 'date_joined', 'role']
>>>>>>> 5b81de312c97f8c81c31149a7945452743572f2c
