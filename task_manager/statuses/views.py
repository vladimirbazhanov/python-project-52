from django.shortcuts import render
from task_manager.statuses.forms import StatusForm


def index(request):
    return render(request, 'statuses/index.html')


def create(request):
    if request.method == 'GET':
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            pass