from django.db import models
from .Project import Project
from .User import User
import uuid

class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f'{self.user.username} in {self.project.name}'
    
    class Meta:
        db_table = 'projectmembers'
