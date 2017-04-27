from django import forms


class AltaForm(forms.Form):
    SEARCH_CHOICES = [('dni', 'DNI'),
                      ('nss', 'NSS')]
    query_choice = forms.ChoiceField(
        label='Escoja tipo de busqueda', choices=SEARCH_CHOICES, widget=forms.RadioSelect())
    nss = forms.CharField(label='NSS', max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
    dni = forms.CharField(label='DNI', max_length=10, widget=forms.TextInput(attrs={'class' : 'form-control'}), required=False)
