from django import forms


class AltaForm(forms.Form):
    SEARCH_CHOICES = [('dni', 'DNI'),
                      ('nss', 'NSS')]
    nss = forms.CharField(label='NSS', max_length=20)
    dni = forms.CharField(label='DNI', max_length=10)
    query_choice = forms.ChoiceField(choices=SEARCH_CHOICES, widget=forms.RadioSelect())
    
