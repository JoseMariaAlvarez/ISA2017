# -*- encoding: utf-8 -*-
from django import forms
from .models import Visita, Comentario
from django.core.validators import MaxValueValidator, MinValueValidator


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
        }
        widgets = {
            'paciente': forms.HiddenInput(attrs={'class' : 'form-control'}),
            'valorINR': forms.FloatField(min_value=0, max_value=1, attrs={'class' : 'form-control'}),
            'dosis': forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha': forms.TextInput(attrs={'class' : 'form-control', 'type':'date'}),
            'duracion': forms.TextInput(attrs={'class' : 'form-control',}),
            'peso': forms.TextInput(attrs={'class' : 'form-control'}),
            'medicacion': forms.Select(attrs={'class' : 'form-control'}),
        }

class ComentarioVisitaForm(forms.ModelForm):
    prefix = 'comentario'
    class Meta:
        model = Comentario
        fields = '__all__'
        labels = {'texto': 'Comentario'}
        widgets = {
            'texto' : forms.TextInput(attrs={'class' : 'form-control'}),
            }
