from rest_framework import viewsets
from ..models import ProjectMember
from ..serializers import ProjectMemberSerializer
from rest_framework.permissions import AllowAny

class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [AllowAny]
