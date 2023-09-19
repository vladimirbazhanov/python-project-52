from django.shortcuts import render, HttpResponseRedirect
from task_manager.labels.forms import LabelForm
from django.views import View
from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.labels.models import Label


class LabelsView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.filter(user_id=request.user.id).order_by('name')
        return render(request, 'labels/index.html', {'labels': labels})


class CreateLabelView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        form = LabelForm()
        return render(request, 'labels/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LabelForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/labels')
        else:
            return render(request,
                          'labels/create.html',
                          {'form': form}
                          )


class UpdateLabelView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        label = Label.objects.get(id=kwargs['id'])
        form = LabelForm(instance=label)
        return render(request,
                      'labels/update.html',
                      {'form': form}
                      )

    def post(self, request, *args, **kwargs):
        label = (Label.objects
                 .filter(user_id=request.user.id)
                 .get(id=kwargs['id']))
        form = LabelForm(instance=label, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/labels')
        else:
            return render(request,
                          'labels/update.html',
                          {'form': form}
                          )


class DeleteLabelView(LoginRequiredWithMessageMixin, View):
    def get(self, request, *args, **kwargs):
        label = (Label.objects
                 .filter(user_id=request.user.id)
                 .get(id=kwargs['id']))
        return render(request,
                      'labels/delete.html',
                      {'label': label}
                      )

    def post(self, request, *args, **kwargs):
        label = (Label.objects
                 .filter(user_id=request.user.id)
                 .get(id=kwargs['id']))
        label.delete()
        return HttpResponseRedirect('/labels')
