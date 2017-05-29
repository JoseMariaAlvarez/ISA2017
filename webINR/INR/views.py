# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .forms import AltaForm, VisitaForm, ComentarioVisitaForm
from webINR import MySQLDriver
from .models import PacienteClinica, Visita
import random
import string
import datetime
from django.db import IntegrityError

# Sobre get_object_or_404():
# https://docs.djangoproject.com/es/1.11/topics/http/shortcuts/#django.shortcuts.get_object_or_404

# @login_required es un decorador que indica que para acceder a la vista debemos estar logueados en el sistema
# De no ser así, nos devolverá la pantalla de inicio de sesión.

@login_required
def index(request):
    return render(request, 'base.html')


@login_required
def ver_ficha(request, nss):
    # Nos muestra la página ficha_de_paciente.html
    connection = MySQLDriver.MySQLConn(
                host="localhost", database="webdb_bdu", username="root", password="root", port=3306)
    cursor = connection.cursor
    query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  nss=\"%s\"' % nss
    cursor.execute(query)
    res = cursor.fetchone()
    #add_to_control = true indica que hay que introducirlo en webdb
    try:
        paciente = PacienteClinica.objects.get(nss=nss)
        request.session['last_patient'] = nss
        add_to_control = False
    except PacienteClinica.DoesNotExist:
        add_to_control = True
            
    context = {'nss': res[0], 'dni': res[1], 'nombre': res[2], 'apellido1': res[3], 'apellido2': res[4], 'direccion': res[5], 'cp': res[6],
               'telefono': res[7], 'ciudad': res[8], 'provincia': res[9], 'pais': res[10], 'fecha_nacimiento': res[11], 'sexo':res[12],
               'add_to_control':add_to_control}
    return render(request, 'pages/ficha_de_paciente.html', context)


@login_required
def dar_alta(request):
    """ A connection to the remote server is issued,
    in order to check whether the data given exists. In case
    it doesn't exist a new user is created. """
        
    # Cuando enviemos datos a través del formulario...
    
    if request.method == 'POST':
        # ...si el formulario es válido...
        # ...establecemos conexión con la base de datos.
        connection = MySQLDriver.MySQLConn(
            host="localhost", database="webdb_bdu", username="root", password="root", port=3306)
        cursor = connection.cursor
        query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo, rango FROM webdb_bdu.paciente WHERE  nss=\"%s\"' % request.POST['nss']
          
        cursor.execute(query)

        res = cursor.fetchone()

        password = ''.join(random.choice(string.lowercase)
                            for i in range(10))
        context = {'nss': res[0], 'dni': res[1], 'nombre': res[2], 'apellido1': res[3],
                   'apellido2': res[4], 'direccion': res[5], 'cp': res[6],
                   'telefono': res[7], 'ciudad': res[8], 'provincia': res[9],
                   'pais': res[10], 'fecha_nacimiento': res[11], 'sexo':res[12],
                   'rango': res[13],}
        #Este try controla que no se meta el mismo paciente dos veces en la DB
        try:
            # Creamos el usuario usando los parámetros obtenidos de la query o
            # lo recuperamos en caso de ya existir (get_or_create())
            paciente = PacienteClinica.objects.get_or_create(
                nss=res[0], dni=res[1], nombre=res[2], apellido_1=res[
                    3], apellido_2=res[4], direccion=res[5], cp=res[6], telefono=res[7],
                ciudad=res[8], provincia=res[8], pais=res[10], fecha_nacimiento=res[11], sexo=res[12], password=password)
            visitas = Visita.objects.filter(paciente_id=paciente.id)
            contex['visitas'] = visitas
        except IntegrityError:
            #Entra por aquí si escribimos directamente la url a mano:
            #ficha/nss donde nss es el nss del paciente
            context['add_to_control'] = True
            context['confirm'] = False

            return render(request, 'pages/ficha_de_paciente.html', context)
        
        request.session['last_patient'] = res[0]
        # connection.close()
        return render(request, 'pages/gestor_de_paciente.html', context)
    else:
        form = AltaForm()
        return render(request, 'pages/buscar_paciente.html', {'form':form, 'error':True})

@login_required
def gestor(request):
    if request.method == 'POST':
        nssValue = request.POST['nss']
        
    else:
        if not request.session['last_patient']:
            render(request, 'pages/buscar_paciente.html')           
        nssValue = request.session['last_patient']

    paciente = PacienteClinica.objects.get(nss = nssValue)
    visitas = Visita.objects.filter(paciente_id=paciente.id)
    context = {'dni': paciente.dni, 'nss': paciente.nss, 'nombre':paciente.nombre,
               'apellido1':paciente.apellido_1, 'apellido2': paciente.apellido_2,
               'direccion':paciente.direccion, 'cp':paciente.cp, 'telefono': paciente.telefono,
               'ciudad':paciente.ciudad, 'provincia':paciente.provincia, 'pais': paciente.pais,
               'fecha_nacimiento':paciente.fecha_nacimiento, 'sexo':paciente.sexo,
               'rango':paciente.rango, 'visitas':visitas}
    return render(request, 'pages/gestor_de_paciente.html', context)
    
@login_required
def buscar(request):
    """ Search in the local DB for DNI and NSS
    information. """
    if request.method == 'POST':
        form = AltaForm(request.POST)
        # ...si el formulario es válido...
        # ...establecemos conexión con la base de datos.
        if form.is_valid():
            connection = MySQLDriver.MySQLConn(
                host="localhost", database="webdb_bdu", username="root", password="root", port=3306)
            cursor = connection.cursor

            query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  dni=\"%s\"' % form.cleaned_data['dato']
            # Ejecutamos la query
            cursor.execute(query)
            # Recuperamos el resultado de la query
            res = cursor.fetchone()
            if not res:
                query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  nss=\"%s\"' % form.cleaned_data['dato']
                cursor.execute(query)
                res = cursor.fetchone()
                if not res:
                    return render(request, 'pages/buscar_paciente.html', {'error' : True, 'form': form})

            paciente = PacienteClinica.objects.get(nss = res[0])
            
            #add_to_control = true indica que hay que añadirlo al control
            if not paciente:
                add_to_control = True
            else:
                add_to_control = False
            
            context = {'nss': res[0], 'dni': res[1], 'nombre': res[2], 'apellido1': res[3], 'apellido2': res[4], 'direccion': res[5], 'cp': res[6],
                       'telefono': res[7], 'ciudad': res[8], 'provincia': res[9], 'pais': res[10], 'fecha_nacimiento': res[11], 'sexo':res[12],
                       'add_to_control':add_to_control}

            request.session['last_patient'] = res[0]
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

@login_required
def crear_visita(request, nss):
    if request.method == 'POST':
        formVisita = VisitaForm(request.POST, prefix='visita')
        formComentario = ComentarioVisitaForm(request.POST, prefix='comentario')
        if formVisita.is_valid() and formComentario.is_valid():  
            comentario = formComentario.save()
            new_visit = Visita(**formVisita.cleaned_data)
            new_visit.comentario_id = comentario.id
            new_visit.save()
            paciente = PacienteClinica.objects.get(nss=nss)
            visitas = Visita.objects.filter(paciente_id=paciente.id)
            context = {'dni': paciente.dni, 'nss': paciente.nss, 'nombre':paciente.nombre,
                       'apellido1':paciente.apellido_1, 'apellido2': paciente.apellido_2,
                       'direccion':paciente.direccion, 'cp':paciente.cp, 'telefono': paciente.telefono,
                       'ciudad':paciente.ciudad, 'provincia':paciente.provincia, 'pais': paciente.pais,
                       'fecha_nacimiento':paciente.fecha_nacimiento, 'sexo':paciente.sexo,
                       'rango': paciente.rango, 'visitas':visitas, 'visit_success':True}
            return render(request, 'pages/gestor_de_paciente.html', context)
        
    paciente = PacienteClinica.objects.get(nss=nss)
    formVisita = VisitaForm(initial = {'paciente': paciente.id}, prefix = 'visita')
    formComentario = ComentarioVisitaForm(prefix = 'comentario')
    context = {'dni': paciente.dni, 'nss': paciente.nss, 'nombre':paciente.nombre,
               'apellido1':paciente.apellido_1, 'apellido2': paciente.apellido_2,
               'direccion':paciente.direccion, 'cp':paciente.cp, 'telefono': paciente.telefono,
               'ciudad':paciente.ciudad, 'provincia':paciente.provincia, 'pais': paciente.pais,
               'fecha_nacimiento':paciente.fecha_nacimiento, 'sexo':paciente.sexo,
               'formVisita':formVisita, 'formComentario':formComentario}
    return render(request, 'pages/crear_visita.html', context)

@login_required
def nuevo_rango(request):
    paciente = PacienteClinica.objects.get(nss=request.session['last_patient'])
    if request.method == 'POST':
        paciente.rango = request.POST['new_range']
        paciente.save()

    visitas = Visita.objects.filter(paciente_id=paciente.id)
    context = {'dni': paciente.dni, 'nss': paciente.nss, 'nombre':paciente.nombre,
               'apellido1':paciente.apellido_1, 'apellido2': paciente.apellido_2,
               'direccion':paciente.direccion, 'cp':paciente.cp, 'telefono': paciente.telefono,
               'ciudad':paciente.ciudad, 'provincia':paciente.provincia, 'pais': paciente.pais,
               'fecha_nacimiento':paciente.fecha_nacimiento, 'sexo':paciente.sexo,
               'rango': paciente.rango, 'visitas':visitas}
    return render(request, 'pages/gestor_de_paciente.html', context)
        
