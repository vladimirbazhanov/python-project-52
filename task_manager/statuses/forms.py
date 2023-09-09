from django import forms
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Status
        fields = ('name', )

