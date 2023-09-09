from django.urls import path
from task_manager.statuses import views

app_name = 'statuses'

urlpatterns = [
    path('', views.StatusesView.as_view(), name='index'),
    path('create/', views.CreateStatusView.as_view(), name='create')
]