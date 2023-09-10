from django.urls import path
from task_manager.labels import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelsView.as_view(), name='index'),
    path('create/', views.CreateLabelView.as_view(), name='create'),
    path('<id>/update/', views.UpdateLabelView.as_view(), name='update'),
    path('<id>/delete/', views.DeleteLabelView.as_view(), name='delete')
]
