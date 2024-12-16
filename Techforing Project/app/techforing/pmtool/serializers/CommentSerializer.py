from rest_framework import serializers
from ..models import Comment, User, Task

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    task = serializers.SlugRelatedField(queryset=Task.objects.all(), slug_field='title')
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']
