from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.conf import settings


class LoginRequiredWithMessageMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return HttpResponseRedirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)