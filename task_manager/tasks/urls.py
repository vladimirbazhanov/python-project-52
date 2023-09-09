from django.urls import path
from task_manager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksView.as_view(), name='index'),
    path('', views.CreateTaskView.as_view(), name='create'),
]