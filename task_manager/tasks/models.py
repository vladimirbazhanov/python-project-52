from django.db import models
from django.conf import settings
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=128)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    executor = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='executor')
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
