from rest_framework import serializers
from backend.models import Task
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'username', 'email', 'text', 'isDone']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'