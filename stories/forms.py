from django import forms
from .models import Story

class StoryCreationForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'characters', 'ages', 'setting', 'theme']
