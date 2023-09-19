from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserForm, UserAuthenticationForm
from django.contrib import auth
from task_manager.mixins import LoginRequiredWithMessageMixin
from .models import User

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
        MSG = 'Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.'
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
            else:
                messages.error(request, MSG)
        else:
            messages.error(request, MSG)
        return HttpResponseRedirect('/')

class LogoutUser(View):
    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect('/')


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
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


class UpdateUserView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        if not request.user.id == user.id:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return HttpResponseRedirect('/users')

        form = UserForm(instance=user)
        return render(request, 'users/update.html', { 'form': form})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        if not request.user.id == user.id:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return HttpResponseRedirect('/users')

        form = UserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Пользователь успешно изменен')
            return HttpResponseRedirect('/users')
        else:
            messages.error(request, 'Ошибка')
            return render(request, 'users/update.html', {'form': form})