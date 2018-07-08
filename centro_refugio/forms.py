from django import forms
from django.forms import ModelForm
from .models import Centro

class CentroRefugioForm(forms.ModelForm):
    
    class Meta:
        model = Centro
        fields = [
            'nombre_centro',
            'visita',
            'mascota',
        ]

        labes = {
            'nombre_centro': 'Nombre Centro',
            'visita': 'Visita',
            'mascota': 'Mascota',
        }

        widgets = {
            'nombre_centro': forms.TextInput(attrs={ 'class': 'form-control'}),
            'visita': forms.Select(attrs={ 'class': 'form-control'}),
            'mascota': forms.Select(attrs={ 'class': 'form-control'}),
        }