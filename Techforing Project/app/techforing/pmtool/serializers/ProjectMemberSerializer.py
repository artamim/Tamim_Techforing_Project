from rest_framework import serializers
from ..models import ProjectMember, Project, User

class ProjectMemberSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    
    class Meta:
        model = ProjectMember
        fields = ['id', 'user', 'project', 'role']
        
    def validate(self, attrs):
        project = attrs['project']
        user = attrs['user']
        if ProjectMember.objects.filter(project=project, user=user).exists():
            raise serializers.ValidationError("This user is already a member of the project.")
        return attrs
