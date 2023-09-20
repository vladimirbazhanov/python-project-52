from django import forms
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    executor = forms.ModelChoiceField(User.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), label='Исполнитель')
    status = forms.ModelChoiceField(Status.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), label='Статус')
    labels = forms.ModelMultipleChoiceField(Label.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-select'}), label='Метки')

    class Meta:
        model = Task
        fields = ('name', 'description', 'executor', 'status', 'labels')

class SearchTaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(User.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    status = forms.ModelChoiceField(Status.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    labels = forms.ModelMultipleChoiceField(Label.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-select'}))
    only_my = forms.BooleanField(label='Только свои задачи')

    class Meta:
        model = Task
        fields = ('executor', 'status', 'labels', 'only_my')