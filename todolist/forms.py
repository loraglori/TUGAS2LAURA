from django import forms
from todolist.models import Task

class TaskForm(forms.Form):
    title = forms.CharField(label="Judul", max_length=100, widget=forms.TextInput(attrs={"id":"input-title"}))
    description = forms.CharField(label="Deskripsi", max_length=250, widget=forms.TextInput(attrs={"id":"input-desc"}))