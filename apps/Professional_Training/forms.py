# forms.py
from django import forms
from .models import Professional_Training

class ProfessionalTrainingForm(forms.ModelForm):
    class Meta:
        model = Professional_Training
        fields = ['title', 'subtitle', 'content', 'date', 'image','level']
    date = forms.DateField(widget=forms.SelectDateWidget())
