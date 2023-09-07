from django.shortcuts import render, HttpResponseRedirect
from task_manager.forms import UserAuthenticationForm
from django.contrib import auth


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        form = UserAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    else:
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
