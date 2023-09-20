from django.urls import path
from task_manager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksView.as_view(), name='index'),
    path('<id>/', views.TaskView.as_view(), name='show'),
    path('create/', views.CreateTaskView.as_view(), name='create'),
    path('<id>/update/', views.UpdateTaskView.as_view(), name='update'),
    path('<id>/delete/', views.DeleteTaskView.as_view(), name='delete')
]
