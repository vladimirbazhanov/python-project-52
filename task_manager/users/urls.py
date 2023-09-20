from django.urls import path
from task_manager.users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersView.as_view(), name='index'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('<id>/update/', views.UpdateUserView.as_view(), name='update'),
    path('<id>/delete/', views.DeleteUserView.as_view(), name='delete')
]
