from django import forms
from .models import Visita

# Alta Form.
class AltaForm(forms.Form):
    SEARCH_CHOICES = [('dni', 'DNI'),
                      ('nss', 'NSS')]
    query_choice = forms.ChoiceField(
        label='Escoja tipo de busqueda', choices=SEARCH_CHOICES, widget=forms.RadioSelect())
    nss = forms.CharField(label='NSS', max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
    dni = forms.CharField(label='DNI', max_length=10, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)

# Inherits from Visita object to instance the database, avoiding duplicates.
class VisitaForm(forms.ModelForm):
	class Meta:
		model = Visita
		fields = '__all__'
