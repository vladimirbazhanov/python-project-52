from django.shortcuts import render, HttpResponseRedirect
from task_manager.statuses.forms import StatusForm
from django.views import View
from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.statuses.models import Status


class StatusesView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.filter(user_id=request.user.id).order_by('name')

        return render(request, 'statuses/index.html', {'statuses': statuses})


class CreateStatusView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/statuses')
        else:
            return render(request, 'statuses/create.html', {'form': form})