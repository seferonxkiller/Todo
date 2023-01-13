from django import forms
from .models import Task


class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']
        # fields = ['title', 'slug', 'content']


