from django import forms

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    edad = forms.IntegerField(max_value = 100 , min_value = 1 )