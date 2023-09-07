from django.urls import path
from task_manager.users.views import index

urlpatterns = [
    path('', index)
]
