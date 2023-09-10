from django import forms
from task_manager.labels.models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Label
        fields = ('name', )
