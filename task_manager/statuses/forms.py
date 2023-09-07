from django import forms

class StatusForm(forms.Form):
    name = forms.CharField(label='Название статуса')
