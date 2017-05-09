# -*- encoding: utf-8 -*-
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

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        labels = {
            'paciente': 'Paciente',
        }
        widgets = {
            'paciente': forms.Select(attrs={'class' : 'form-control'}),
            'valorINR': forms.TextInput(attrs={'class' : 'form-control'}),
            'dosis': forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha': forms.TextInput(attrs={'class' : 'form-control'}),
            'duracion': forms.TextInput(attrs={'class' : 'form-control'}),
            'peso': forms.TextInput(attrs={'class' : 'form-control'}),
            'rango': forms.TextInput(attrs={'class' : 'form-control'}),
            'comentario': forms.Select(attrs={'class' : 'form-control'}),
            'medicacion': forms.Select(attrs={'class' : 'form-control'}),
        }
