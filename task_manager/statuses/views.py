from django.shortcuts import render
from task_manager.statuses.forms import StatusForm


def index(request):
    return render(request, 'statuses/index.html')


def create(request):
    form = StatusForm()
    return render(request, 'statuses/create.html')