from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from task_manager.statuses.forms import StatusForm
from django.views import View
from django.views.generic.list import ListView
from django.contrib import messages
from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusesView(LoginRequiredWithMessageMixin, ListView):
    model = Status

    def get_queryset(self):
        return Status.objects.filter(user_id=self.request.user.id)


class CreateStatusView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request,
                      'statuses/create.html',
                      {'form': form}
                      )

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.info(request, _('Status successfully created'))
            return HttpResponseRedirect('/statuses')
        else:
            return render(request,
                          'statuses/create.html',
                          {'form': form}
                          )


class UpdateStatusView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        status = Status.objects.get(id=kwargs['id'])
        form = StatusForm(instance=status)
        return render(request,
                      'statuses/update.html',
                      {'form': form}
                      )

    def post(self, request, *args, **kwargs):
        status = (Status.objects
                  .filter(user_id=request.user.id)
                  .get(id=kwargs['id'])
                  )
        form = StatusForm(instance=status, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('Status successfully updated'))
            return HttpResponseRedirect('/statuses')
        else:
            return render(request,
                          'statuses/update.html',
                          {'form': form}
                          )


class DeleteStatusView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        status = Status.objects.get(id=kwargs['id'])
        if status.task_set.exists():
            messages.error(request, _('Can not delete status assigned to task.'))
            return HttpResponseRedirect(reverse('statuses:index'))
        else:
            return render(request, 'statuses/delete.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status = Status.objects.get(id=kwargs['id'])
        if status.task_set.exists():
            messages.error(request, _('Can not delete status assigned to task.'))
        else:
            status.delete()
            messages.info(request, _('Status successfully deleted'))
        return HttpResponseRedirect(reverse('statuses:index'))
