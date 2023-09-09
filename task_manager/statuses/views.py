from django.shortcuts import render
from task_manager.statuses.forms import StatusForm
from django.views import View
from task_manager.mixins import LoginRequiredWithMessageMixin


class StatusesView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/index.html')


class CreateStatusView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            pass