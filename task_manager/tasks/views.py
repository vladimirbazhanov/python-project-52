from django.shortcuts import render
from django.views import View
from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.tasks.forms import TaskForm

class TasksView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')


class CreateTaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})