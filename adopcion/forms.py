from django import forms

class PersonaForm(forms.ModelForm):
    
    class Meta:
        
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]

        labes = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={ 'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={ 'class': 'form-control'}),
            'edad': forms.TextInput(attrs={ 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={ 'class': 'form-control'}),
            'email': forms.EmailField(),
            'domicilio': forms.TextInput(attrs={ 'class': 'form-control'}),
        }

