# -*- encoding: utf-8 -*-
from django import forms
from .models import Visita, Comentario


# Alta Form.
class AltaForm(forms.Form):

    dato = forms.CharField(label='DNI o NSS', max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=True)

class VisitaForm(forms.ModelForm):
    prefix = 'visita'
    class Meta:
        model = Visita
        fields = ['paciente', 'valorINR', 'dosis', 'duracion', 'peso', 'fecha','medicacion']
        labels = {
            'paciente': 'Paciente',
            'duracion': 'Duración (días)',
            'peso': 'Peso (kg)',
            'dosis': 'Dosis (mg/semana)',
            'valorINR' : 'Valor INR',
            'medicacion': 'Medicación',
        }
        widgets = {
            'paciente': forms.HiddenInput(attrs={'class' : 'form-control'}),
            'valorINR': forms.NumberInput(attrs={'class' : 'form-control','min': 0, 'max': 5, 'step':0.1}),
            'dosis': forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha': forms.TextInput(attrs={'class' : 'form-control', 'id':'fecha', 'onchange':'cambiarDuracion()'}),
            'duracion': forms.TextInput(attrs={'class' : 'form-control','id':'duracion', 'onchange':'cambiarFecha()',}),
            'peso': forms.TextInput(attrs={'class' : 'form-control'}),
            'medicacion': forms.Select(attrs={'class' : 'form-control'}),
        }

class ComentarioVisitaForm(forms.ModelForm):
    prefix = 'comentario'
    class Meta:
        model = Comentario
        fields = ['texto', 'autor']
        labels = {'texto': 'Comentario'}
        widgets = {
            'texto' : forms.Textarea(attrs={'class' : 'form-control', 'rows':'2'}),
            'autor' : forms.TextInput(attrs={'hidden':'hidden'}),
            }
