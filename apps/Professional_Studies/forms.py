from django import forms
from .models import Professional_Studies

class ProfessionalStudiesForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2015, 2100))  # Ajusta el rango a tus necesidades
    )
    class Meta:
        model = Professional_Studies
        fields = ['titulo','title', 'subtitulo', 'subtitle', 'contenido', 'content', 'date', 'image','level', 'website']
