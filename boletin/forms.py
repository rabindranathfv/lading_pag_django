from django import forms

from .models import Registrado

class RegModalForm(forms.ModelForm):
    class Meta:
        # hacemos referencia al modelo y lo utilizamos como model form
        model = Registrado
        # listamos todos los campos que queremos utilizar
        fields = ["nombre","email"]

        # self hace referencia al objeto de la clase
        def clean_nombre(self):
            nombre = self.cleaned_data.get("email")
            return nombre

class ContactForm(forms.Form):
    # si se deja required = false el campo deja de ser obligatorio, y sin colocar POST or None en el views.py
    nombre = forms.CharField(max_length=255 , required = False)
    email = forms.EmailField(required = True)
    mensj = forms.CharField(widget=forms.Textarea)