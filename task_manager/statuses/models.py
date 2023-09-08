from django.db import models
from task_manager.users.models import User
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
