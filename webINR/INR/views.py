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
def ver_ficha(request):
    return render(request, 'pages/ficha_de_paciente.html')


@login_required
def dar_alta(request):
    if request.method == 'POST':
        form = AltaForm(request.POST)

        if form.is_valid():
            connection = MySQLDriver.MySQLConn(
                host="localhost", database="usuariossanitarios", username="root", password="angel", port=3306)
            cursor = connection.cursor

            if form.cleaned_data['query_choice'] == 'dni':
                query = 'SELECT nss,dni,nombre,apellido1 FROM pacientes WHERE dni=\"%s\"' % form.cleaned_data[
                    'dni']
            else:
                query = 'SELECT nss,dni,nombre,apellido1 FROM pacientes WHERE nss=\"%s\"' % form.cleaned_data[
                    'nss']

            cursor.execute(query)
            row = cursor.fetchone()
            password = ''.join(random.choice(string.lowercase)
                               for i in range(10))
            PacienteClinica.objects.get_or_create(
                nss=row[0], dni=row[1], nombre=row[2], apellido_1=row[3], password=password)

            return HttpResponse('Paciente dado de alta en la base de datos.')
    else:
        form = AltaForm()

    return render(request, 'pages/alta_de_paciente.html', {'form': form})

@login_required
def buscar(request):
    if request.method == 'POST':
        form = AltaForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['query_choice'] == 'dni':
                res = PacienteClinica.objects.get(dni=form.cleaned_data['dni'])
                return render(request, template_name='pages/resultado_busqueda.html', context={'nss': res.nss, 'dni': res.dni, 'nombre': res.nombre, 'apellido1': res.apellido_1})
            else:
                res = PacienteClinica.objects.get(nss=form.cleaned_data['nss'])
                return render(request, template_name='pages/resultado_busqueda.html', context={'nss': res.nss, 'dni': res.dni, 'nombre': res.nombre, 'apellido1': res.apellido_1})
    else:
        form = AltaForm()

    return render(request, 'pages/buscar_paciente.html', {'form': form})
