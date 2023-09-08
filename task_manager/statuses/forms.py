from django import forms

class StatusForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
