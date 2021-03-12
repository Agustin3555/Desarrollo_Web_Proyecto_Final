from django.forms import ModelForm
from .models import Usuario


class PersonaForm(ModelForm):
	class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'sexo', 'provincia', 'ciudad', 'email']
        labels = {'sexo': 'Sexo',
                  'provincia': 'Provincia',
                  'ciudad': 'Ciudad'}