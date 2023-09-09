from django import forms
from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ('name', 'description')