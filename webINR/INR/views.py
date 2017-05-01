from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AltaForm, VisitaForm
from webINR import MySQLDriver
from models import PacienteClinica, Visita
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

            connection.close()
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


@login_required
def get_visitas(request, nss):
    if request.method == 'GET':
        res = Visita.objects.filter(paciente__nss=nss)
        return render(request, template_name='pages/resultado_visita.html', context={'resultados': res})


@login_required
def cambiar_visita(request, id):
    obj = Visita.objects.get(id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return HttpResponse('Visita actualizada con exito')

    else:
        obj = Visita.objects.get(id=id)
        form = VisitaForm(initial={'id': obj.id, 'fecha': obj.fecha, 'valorINR': obj.valorINR,
                                   'dosis': obj.dosis, 'duracion': obj.duracion, 'peso': obj.peso, 'rango': obj.rango, 'paciente': obj.paciente, 'comentario': obj.comentario, 'medicacion': obj.medicacion})
    return render(request, 'pages/modificar_visitas.html', {'form': form, 'id': id})


@login_required
def get_datos_demograficos(request, nss):
    if request.method == 'POST':
        connection = MySQLDriver.MySQLConn(
            host="localhost", database="usuariossanitarios", username="root", password="angel", port=3306)
        cursor = connection.cursor

        query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM pacientes WHERE nss=%s' % nss
        cursor.execute(query)
        row = cursor.fetchone()
        context = {'nss': row[0], 'dni': row[1], 'nombre': row[2], 'apellido1': row[3], 'apellido2': row[4], 'direccion': row[5], 'cp': row[
            6], 'telefono': row[7], 'ciudad': row[8], 'provincia': row[9], 'pais': row[10], 'fecha_nacimiento': row[11], 'sexo': row[12]}
        return render(request, 'pages/datos_demograficos.html', context)
