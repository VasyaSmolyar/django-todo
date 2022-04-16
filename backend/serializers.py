from rest_framework import serializers
from backend.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'username', 'email', 'text', 'isDone']