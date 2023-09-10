from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserForm
from django.contrib import auth


def index(request):
    User = get_user_model()

    users = User.objects.all()
    context = {'users': users}

    return render(request, 'users/index.html', context)


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