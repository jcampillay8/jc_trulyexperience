from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *



class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    class Meta:
        model = BlogModel
        fields = ['title', 'content']


