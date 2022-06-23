from django import forms

class frameForm(forms.Form):
    title = forms.CharField(max_length=30)

class taskForm(forms.Form):
    title = forms.CharField(max_length=30)
    frame = forms.CharField(widget=forms.HiddenInput())