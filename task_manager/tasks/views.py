from django.shortcuts import render
from django.views import View
from task_manager.mixins import LoginRequiredWithMessageMixin


class TasksView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')


class CreateTaskView(LoginRequiredWithMessageMixin, View):
    pass