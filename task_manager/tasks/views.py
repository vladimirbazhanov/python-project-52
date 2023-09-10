from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class TasksView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/index.html', {'tasks': tasks})


class CreateTaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks')
        else:
            return render(request, 'tasks/create.html', {'form': form})


class UpdateTaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(user_id=request.user.id).get(id=kwargs['id'])
        form = TaskForm(instance=task)
        return render(request, 'tasks/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        task = Task.objects.filter(user_id=request.user.id).get(id=kwargs['id'])
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks')
        else:
            return render(request, 'tasks/update.html', {'form': form})


class DeleteTaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(user_id=request.user.id).get(id=kwargs['id'])
        return render(request, 'tasks/delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = Task.objects.filter(user_id=request.user.id).get(id=kwargs['id'])
        task.delete()
        return HttpResponseRedirect('/tasks')