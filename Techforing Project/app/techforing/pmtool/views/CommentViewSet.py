from rest_framework import viewsets
from ..models import Comment
from ..serializers import CommentSerializer
from rest_framework.permissions import AllowAny

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
