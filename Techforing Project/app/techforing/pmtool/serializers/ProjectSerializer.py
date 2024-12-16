from rest_framework import serializers
from ..models import User, Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']
