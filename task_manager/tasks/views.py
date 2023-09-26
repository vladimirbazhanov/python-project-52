from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.tasks.forms import TaskForm, SearchTaskForm
from task_manager.tasks.models import Task
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class TasksView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = SearchTaskForm(data=request.GET)
        tasks = Task.objects
        if form.data.get('status'):
            tasks = tasks.filter(status=form.data['status'])
        if form.data.get('executor'):
            tasks = tasks.filter(executor=form.data['executor'])
        if form.data.get('label'):
            tasks = tasks.filter(labels=form.data['label'])
        if form.data.get('only_my'):
            tasks = tasks.filter(user_id=request.user.id)
        return render(request, 'tasks/index.html', {'tasks': tasks.all(), 'form': form})


class TaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        return render(request, 'tasks/show.html', {'task': task})


class CreateTaskView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.info(request, _('Task successfully created'))  # Задача успешно создана
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/create.html', {'form': form})


class UpdateTaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        form = TaskForm(instance=task)
        return render(request, 'tasks/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('Task successfully updated'))
            return HttpResponseRedirect('/tasks')
        else:
            return render(request, 'tasks/update.html', {'form': form})


class DeleteTaskView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        if task.user_id == request.user.id:
            return render(request, 'tasks/delete.html', {'task': task})
        else:
            messages.error(request, _('Only owner can update task'))
            return HttpResponseRedirect('/tasks')

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        if task.user_id == request.user.id:
            task.delete()
            messages.info(request, _('Task successfully deleted'))
        else:
            messages.error(request, _('Only owner can delete task'))
        return HttpResponseRedirect('/tasks')
