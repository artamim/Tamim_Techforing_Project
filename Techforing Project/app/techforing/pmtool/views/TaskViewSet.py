from rest_framework import viewsets
from ..models import Task
from ..serializers import TaskSerializer
from rest_framework.permissions import AllowAny

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]