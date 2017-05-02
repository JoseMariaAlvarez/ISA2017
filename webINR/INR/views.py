# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .forms import AltaForm, VisitaForm
from webINR import MySQLDriver
from models import PacienteClinica, Visita
import random
import string

## @login_required es un decorador que indica que para acceder a la vista debemos estar logueados en el sistema
## De no ser así, nos devolverá la pantalla de inicio de sesión.

@login_required
def index(request):
    return render(request, 'base.html')


@login_required
def ver_ficha(request):
    ## Nos muestra la página ficha_de_paciente.html
    return render(request, 'pages/ficha_de_paciente.html')


@login_required
def dar_alta(request):
    """ A connection to the remote server is issued,
    in order to check whether the data given exists. In case
    it doesn't exist a new user is created. """

    if request.method == 'POST':  ## Cuando enviemos datos a través del formulario...
        form = AltaForm(request.POST)

        if form.is_valid():  ## ...si el formulario es válido...
            ## ...establecemos conexión con la base de datos.
            connection = MySQLDriver.MySQLConn(
                host="localhost", database="usuariossanitarios", username="root", password="root", port=3306)
            cursor = connection.cursor

            ## La query cambiará según estemos buscando por dni o por nss
            if form.cleaned_data['query_choice'] == 'dni':
                query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM pacientes WHERE  dni=\"%s\"' % form.cleaned_data[
                    'dni']
            else:
                query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM pacientes WHERE nss=\"%s\"' % form.cleaned_data[
                    'nss']

            ## Ejecutamos la query
            cursor.execute(query)

            ## Recuperamos el resultado de la query
            row = cursor.fetchone()

            ## Creamos una contraseña aleatoria
            password = ''.join(random.choice(string.lowercase)
                               for i in range(10))

            ## Creamos el usuario usando los parámetros obtenidos de la query o lo recuperamos en caso de ya existir (get_or_create())
            PacienteClinica.objects.get_or_create(
                nss=row[0], dni=row[1], nombre=row[2], apellido_1=row[3], apellido_2=row[4], direccion=row[5], cp=row[6], telefono=row[7],
                ciudad=row[8], provincia=row[8], pais=row[10], fecha_nacimiento=row[11], sexo=row[12], password=password)

            #connection.close()
            return render(request, 'pages/alta_de_paciente.html', {'success': 'Paciente dado de alta en la base de datos'})
    else:
        form = AltaForm()

    ## Por defecto, la vista dar_alta nos muestra la página alta_de_paciente.html
    ## Dentro de ésta página encontramos un formulario 'form' que se corresponde con la clase AltaForm dentro de forms.py
    return render(request, 'pages/alta_de_paciente.html', {'form': form})


@login_required
def buscar(request):
    """ Search in the local DB for DNI and NSS
    information. """
    if request.method == 'POST':
        form = AltaForm(request.POST)

        if form.is_valid():
            ## Sobre get_object_or_404(): https://docs.djangoproject.com/es/1.11/topics/http/shortcuts/#django.shortcuts.get_object_or_404
            if form.cleaned_data['query_choice'] == 'dni':
                res = get_object_or_404(PacienteClinica, dni=form.cleaned_data['dni'])
            else:
                res = get_object_or_404(PacienteClinica, nss=form.cleaned_data['nss'])

            visitas = Visita.objects.filter(paciente__nss=res.nss)

            context = {'nss': res.nss, 'dni': res.dni, 'nombre': res.nombre, 'apellido1': res.apellido_1, 'apellido2': res.apellido_2, 'direccion': res.direccion, 'cp': res.cp,
                    'telefono': res.telefono, 'ciudad': res.ciudad, 'provincia': res.provincia, 'pais': res.pais, 'fecha_nacimiento': res.fecha_nacimiento, 'sexo': res.sexo,
                    'visitas': visitas}

            return render(request, 'pages/ficha_de_paciente.html', context)
    else:
        form = AltaForm()

    return render(request, 'pages/buscar_paciente.html', {'form': form})


@login_required
def cambiar_visita(request, id):
    """ Allowing for Visita objects modification,
    including all the parameters belonging to the
    given patient """

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
