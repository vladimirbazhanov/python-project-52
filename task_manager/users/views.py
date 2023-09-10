from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserForm, UserAuthenticationForm
from django.contrib import auth

class UsersView(View):
    def get(self, request, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()
        return render(request, 'users/index.html', {'users': users})


class LoginUser(View):
    def get(self, request, *args, **kwargs):
        form = UserAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')


class LogoutUser(View):
    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect('/')


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'users/create.html', {'form': form})