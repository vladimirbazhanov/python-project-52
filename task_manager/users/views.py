from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    users = User.objects.all()
    context = {'users': users}

    return render(request, 'users/index.html', context)
