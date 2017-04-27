from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AltaForm
from webINR import MySQLDriver
from models import PacienteClinica
import random
import string


@login_required
def index(request):
    return render(request, 'base.html')


@login_required
def ficha(request):
    return render(request, 'pages/ficha_de_paciente.html')


@login_required
def dar_alta(request):
    if request.method == 'POST':
        form = AltaForm(request.POST)

        if form.is_valid():
            connection = MySQLDriver.MySQLConn(
                host="localhost", database="usuariossanitarios", username="root", password="root", port=3306)
            cursor = connection.cursor
            if form.cleaned_data['query_choice'] == 'dni':
                query = 'SELECT nss,dni,nombre,apellido1 FROM pacientes WHERE dni=\"%s\"' % form.cleaned_data[
                    'dni']
                cursor.execute(query)
                row = cursor.fetchone()
                password = ''.join(random.choice(string.lowercase)
                                   for i in range(10))
                PacienteClinica.objects.get_or_create(
                    nss=row[0], dni=row[1], nombre=row[2], apellido_1=row[3], password=password)
            else:
                query = 'SELECT nss,dni,nombre,apellido1 FROM pacientes WHERE nss=\"%s\"' % form.cleaned_data[
                    'nss']
                cursor.execute(query)
                row = cursor.fetchone()
                password = ''.join(random.choice(string.lowercase)
                                   for i in range(10))
                PacienteClinica.objects.get_or_create(
                    nss=row[0], dni=row[1], nombre=row[2], apellido_1=row[3], password=password)

            return HttpResponse('User created')
    else:
        form = AltaForm()

    return render(request, 'alta.html', {'form': form})
