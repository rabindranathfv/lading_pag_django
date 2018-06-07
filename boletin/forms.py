from django import forms

class RegForm(forms.Form):
    # si se deja required = false el campo deja de ser obligatorio, y sin colocar POST or None en el views.py
    nombre = forms.CharField(max_length=255 , required = False)
    edad = forms.IntegerField(max_value = 100 , min_value = 1 )#, required = False)