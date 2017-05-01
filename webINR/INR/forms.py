from django import forms
from .models import Visita

class AltaForm(forms.Form):
    SEARCH_CHOICES = [('dni', 'DNI'),
                      ('nss', 'NSS')]
    query_choice = forms.ChoiceField(
        label='Escoja tipo de busqueda', choices=SEARCH_CHOICES, widget=forms.RadioSelect())
    nss = forms.CharField(label='NSS', max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
    dni = forms.CharField(label='DNI', max_length=10, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)

"""class Visita(forms.Form):
	valorINR = forms.DecimalField(label='Valor INR', max_digits=20, decimal_places=10)
	fecha = forms.DateField(label='Fecha')
	dosis = forms.DecimalField(label='Dosis', max_digits=20, decimal_places=10)
	duracion = forms.CharField(label='Duracion', max_length=45)
	peso = forms.DecimalField(label='Peso', max_digits=20, decimal_places=10)
	rango = forms.CharField(label='Rango', max_length=45)""" 


class VisitaForm(forms.ModelForm):
	class Meta:
		model = Visita
		fields = '__all__'