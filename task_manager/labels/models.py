from django.db import models
from django.conf import settings


class Label(models.Model):
    name = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
