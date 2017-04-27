from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'base.html')

@login_required
def ficha(request):
    return render(request, 'pages/ficha_de_paciente.html')
