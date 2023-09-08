from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def index(request):
    User = get_user_model()

    users = User.objects.all()
    context = {'users': users}

    return render(request, 'users/index.html', context)
