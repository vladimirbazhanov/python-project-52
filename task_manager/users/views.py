from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserForm, UserAuthenticationForm
from django.contrib import auth
from task_manager.mixins import LoginRequiredWithMessageMixin
from .models import User
from django.utils.translation import gettext_lazy as _


class ListUsersView(View):
    def get(self, request, *args, **kwargs):
        User = get_user_model()
        users = User.objects.all()
        return render(request, 'users/index.html', {'users': users})


class LoginUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        MSG = _('Please, enter correct username and password')
        form = UserAuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                messages.info(request, _('You are signed in'))
                auth.login(request, user)
            else:
                messages.error(request, MSG)
        else:
            messages.error(request, MSG)
        return HttpResponseRedirect('/')


class LogoutUserView(View):
    def post(self, request, *args, **kwargs):
        auth.logout(request)
        messages.info(request, _('You are signed out'))
        return HttpResponseRedirect('/')


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = auth.authenticate(username=username, password=password)
            # auth.login(request, user)
            messages.info(request, 'Пользователь успешно зарегистрирован')
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'users/create.html', {'form': form})


class UpdateUserView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        if not request.user.id == user.id:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return HttpResponseRedirect('/users')

        form = UserForm(instance=user)
        return render(request, 'users/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        if not request.user.id == user.id:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return HttpResponseRedirect('/users')

        form = UserForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Пользователь успешно изменен')
            return HttpResponseRedirect('/users')
        else:
            messages.error(request, 'Ошибка')
            return render(request, 'users/update.html', {'form': form})


class DeleteUserView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        if user.id == request.user.id:
            return render(request, 'users/delete.html', {'user': user})
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return HttpResponseRedirect('/users')

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        if user.id == request.user.id:
            messages.info(request, 'Пользователь успешно удален')
            user.delete()
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return HttpResponseRedirect('/users')
        return HttpResponseRedirect('/users')
