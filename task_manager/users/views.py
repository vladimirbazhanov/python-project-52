from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from task_manager.users.models import User
from task_manager.users.forms import UserForm


def index(request):
    User = get_user_model()

    users = User.objects.all()
    context = {'users': users}

    return render(request, 'users/index.html', context)


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})