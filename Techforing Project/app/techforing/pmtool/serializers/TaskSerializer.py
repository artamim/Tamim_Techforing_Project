from rest_framework import serializers
from ..models import Task, Project, User

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']
