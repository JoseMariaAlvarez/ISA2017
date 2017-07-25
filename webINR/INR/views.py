# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import formats
from .forms import AltaForm, VisitaForm, ComentarioVisitaForm
from webINR import MySQLDriver
from .models import PacienteClinica, Visita, Comentario, Medicacion, Diagnostico
from django.core import serializers
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
                host='localhost', database='webdb_bdu', username='root', password='control de INR', port=3306)
    cursor = connection.cursor
    query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  nss=\"%s\"' % nss
    cursor.execute(query)
    res = cursor.fetchone()
    #add_to_control = true indica que hay que introducirlo en webdb
    try:
        paciente = PacienteClinica.objects.get(nss=nss)
        request.session['nss'] = nss
        add_to_control = False
        request.session['id'] = paciente.id
    except PacienteClinica.DoesNotExist:
        add_to_control = True

    #add_to_control = True indica que dicho paciente se va a añadir al control        
    context = {'add_to_control':add_to_control}
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
            host='localhost', database='webdb_bdu', username='root', password='control de INR', port=3306)
        cursor = connection.cursor
        # Creamos la query a partir del nss del POST
        query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  nss=\"%s\"' % request.POST['nss']

        #Ejecutamos la query 
        cursor.execute(query)
        # Recuperamos el objeto (paciente) resultante de la query
        res = cursor.fetchone()
        #Creamos una password random
        password = ''.join(random.choice(string.lowercase)
                            for i in range(10))
        #Este try controla que no se meta el mismo paciente dos veces en la DB
        try:
            # Creamos el usuario usando los parámetros obtenidos de la query o
            # lo recuperamos en caso de ya existir (get_or_create())
            paciente = PacienteClinica.objects.get_or_create(
                nss=res[0], dni=res[1], nombre=res[2], apellido_1=res[
                    3], apellido_2=res[4], direccion=res[5], cp=res[6], telefono=res[7],
                ciudad=res[8], provincia=res[8], pais=res[10], fecha_nacimiento=res[11],
                sexo=res[12], password=password, rango_inf='-', rango_sup='-')
            paciente = PacienteClinica.objects.get(nss=res[0])
            insertarPacienteSesion(request, paciente)
            visitas = Visita.objects.filter(paciente_id= paciente.id).order_by('id').reverse()
            context = {'visitas' : visitas}
            
        except IntegrityError:
            #Entra por aquí si escribimos directamente la url a mano:
            #ficha/nss donde nss es el nss del paciente
            context = {'add_to_control' : False}

            return render(request, 'pages/ficha_de_paciente.html', context)
        
        request.session['nss'] = res[0]
        # connection.close()
        return render(request, 'pages/gestor_de_paciente.html', context)
    else:
        form = AltaForm()
        return render(request, 'pages/buscar_paciente.html', {'form':form, 'error':True})

@login_required
def gestor(request):
    #Si venimos desde un formulario, recogemos el nss por post
    if request.method == 'POST':
        #Recogemos el nss desde el post
        nssValue = request.POST['nss']
        paciente = PacienteClinica.objects.get(nss=nssValue)
        insertarPacienteSesion(request, paciente)

    # Si venimos desde un hiperenlace
    else:
        #Si el paciente no está en sesion
        #Redirigimos a buscar paciente mostrando un error
        if not 'last_patient' in request.session:
            form = AltaForm()
            return render(request, 'pages/buscar_paciente.html', {'form':form, 'search_first':True})           
        #Recogemos el nss de sesion
        nssValue = request.session['nss']

    # Buscamos el paciente,
    try:
        paciente = PacienteClinica.objects.get(nss = nssValue)
    except PacienteClinica.DoesNotExist:
        return HttpResponseRedirect('/ficha/%s' % nssValue)
    # Buscamos las visitas del paciente
    visitas = Visita.objects.filter(paciente_id=paciente.id).order_by('id').reverse()
    # Buscamos los diagnósticos del paciente
    diagnosticos = paciente.diagnosticos.all()
    # Enviamos todos los diagnósticos para generar el formulario para añadir nuevo diagnóstico
    all_diagnostics = Diagnostico.objects.all()
    #Construímos los datos que se usan en el template
    context = {'visitas':visitas, 'diagnosticos':diagnosticos, 'all_diagnostics':all_diagnostics}
    return render(request, 'pages/gestor_de_paciente.html', context)
    

def insertarPacienteSesion(request, paciente):
        request.session['last_patient'] = True
        request.session['id'] = paciente.id
        request.session['nss'] = paciente.nss
        request.session['dni'] = paciente.dni
        request.session['nombre'] = paciente.nombre
        request.session['apellido1'] = paciente.apellido_1
        request.session['apellido2'] = paciente.apellido_2
        request.session['direccion'] = paciente.direccion
        request.session['cp'] = paciente.cp
        request.session['telefono'] = paciente.telefono
        request.session['ciudad'] = paciente.ciudad
        request.session['provincia'] = paciente.provincia
        request.session['pais'] = paciente.pais
        request.session['fecha_nacimiento'] = str(paciente.fecha_nacimiento)
        request.session['sexo'] = paciente.sexo
        request.session['rango_inf'] = paciente.rango_inf
        request.session['rango_sup'] = paciente.rango_sup

@login_required
def buscar(request):
    """ Search in the local DB for DNI and NSS
    information. """
    if request.method == 'POST':
        form = AltaForm(request.POST)
        # ...si el formulario es válido...
        # ...establecemos conexión con la base de datos.
        if form.is_valid():
            dato = form.cleaned_data['dato']
            connection = MySQLDriver.MySQLConn(
                host='localhost', database='webdb_bdu', username='root', password='control de INR', port=3306)
            cursor = connection.cursor
            #Buscamos el paciente cuyo DNI sea igual que el dato que se envía por POST
            query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  dni=\"%s\"' % dato
            # Ejecutamos la query
            cursor.execute(query)
            # Recuperamos el paciente resultante de la query
            res = cursor.fetchone()
            #¿Hay algún paciente que corresponda con la descripción?
            if not res:
                #Si no existe ningún paciente con ese DNI, buscamos por NSS
                query = 'SELECT nss, dni, nombre, apellido1, apellido2, direccion, cp, telefono, ciudad, provincia, pais, fecha_nacimiento, sexo FROM webdb_bdu.paciente WHERE  nss=\"%s\"' % dato
                cursor.execute(query)
                res = cursor.fetchone()

                if not res:
                    #Si no hay ningún paciente con ese NSS, ni con ese DNI, ni con esa fecha, redirigimos a buscar
                    #Ha habido algún error
                    return render(request, 'pages/buscar_paciente.html', {'error' : True, 'form': form})

            #En este punto, tenemos un paciente (res) que coincide(dni o nss)
            #Buscamos en webdb si el paciente está dado de alta
            try:
                paciente = PacienteClinica.objects.get(nss = res[0])
                add_to_control = False
            except PacienteClinica.DoesNotExist:
                add_to_control = True
            
            #add_to_control = true indica que hay que añadirlo al control
            
            context = {'add_to_control':add_to_control}

            # request.session['last_patient'] = None
            context['nss'] = res[0]
            context['dni'] = str(res[1])
            context['nombre'] = str(res[2])
            context['apellido1'] = str(res[3])
            context['apellido2'] = str(res[4])
            context['direccion'] = str(res[5])
            context['cp'] = res[6]
            context['telefono'] = str(res[7])
            context['ciudad'] = str(res[8])
            context['provincia'] = str(res[9])
            context['pais'] = str(res[10])
            context['fecha_nacimiento'] = str(res[11])
            context['sexo'] = str(res[12])
            
            return render(request, 'pages/ficha_de_paciente.html', context)
    else:
        form = AltaForm()

    return render(request, 'pages/buscar_paciente.html', {'form': form})

@login_required
def buscar_fecha(request):
    if request.method == 'POST':
        dato = request.POST['fecha_visita']
        try:
            pacientes = PacienteClinica.objects.filter(visita__fecha= str(dato)).distinct()
        except ValueError:
            return render(request, 'pages/buscar_paciente.html', {'error' : True, 'form': AltaForm()})

        if not pacientes:
            return render(request, 'pages/buscar_paciente.html', {'error' : True, 'form': AltaForm()})
            
        return render(request, 'pages/ficha_de_paciente.html', {'pacientes': pacientes, 'add_to_control': False})


@login_required
def cambiar_visita(request, id):
    """ Allowing for Visita objects modification,
    including all the parameters belonging to the
    given patient """

    obj = Visita.objects.get(id=id)
    error_formulario = None
    if request.method == 'POST':
        # Creo el formulario con los datos del post pero instanciando a la visita ya guardada
        visitaForm = VisitaForm(request.POST, instance=obj)
        # Creo el formulario del comentario a partir de los datos del POST
        comentarioForm = ComentarioVisitaForm(request.POST)
        if visitaForm.is_valid() and comentarioForm.is_valid():
            new_visita = visitaForm.save()
            comentario = Comentario(**comentarioForm.cleaned_data)
            comentario.visita_id = new_visita.id
            comentario.save()
            # Recuperamos las visitas del paciente.
            visitas = Visita.objects.filter(paciente_id = request.session['id']).order_by('id').reverse()
            return render(request, 'pages/gestor_de_paciente.html', {'visitas' : visitas, 'visit_change_success':True})

        else:
            error_formulario = "El formulario no se ha enviado correctamente. Compruebe los datos introducidos"
    formVisita = VisitaForm(initial={'id': obj.id, 'fecha': obj.fecha,
                               'valorINR': obj.valorINR, 'dosis': obj.dosis,
                               'duracion': obj.duracion, 'peso': obj.peso,
                               'paciente': obj.paciente, 'medicacion': obj.medicacion,
                               })
    comentarios = Comentario.objects.filter(visita_id = id)
    all_comments = ""
    
    for comentario in comentarios:
        if comentario.texto is not None:
            all_comments = all_comments + "-" + comentario.autor + ": " + comentario.texto + "\n --- \n"
      
    formComentario = ComentarioVisitaForm(initial = {'autor': request.user.first_name +' ' + request.user.last_name}, prefix = 'comentario')

    return render(request, 'pages/modificar_visitas.html', {'formVisita': formVisita, 'comentariosAntiguos':all_comments, 
                        'formComentario': formComentario, 'id': id, 'error_formulario': error_formulario})

@login_required
def crear_visita(request, nss):
    #Cargamos nuevamente los datos del último paciente
    # para que se muestre en gestor_de_paciente o en crear_visita
    paciente = PacienteClinica.objects.get(nss=nss)

    #¿Se llega aquí mediante un submit con método POST?
    if request.method == 'POST':
        #Creamos los formularios de visita y comentario a partir de los datos enviados por post
        # Utilizamos prefix para identificar los datos enviados con su correspondiente form
        formVisita = VisitaForm(request.POST, prefix='visita')
        formComentario = ComentarioVisitaForm(request.POST, prefix='comentario')

        #¿Son ambos formularios válidos?
        if formVisita.is_valid() and formComentario.is_valid():  
            new_visita = formVisita.save()
            comentario = Comentario(**formComentario.cleaned_data)
            comentario.visita_id = new_visita.id
            comentario.save()
            """
            comentario = formComentario.save()
            #Crear una visita cómodamente con los datos del formulario
            new_visit = Visita(**formVisita.cleaned_data)
            #Añadimos el id del nuevo comentario que se ha creado
            new_visit.comentario_id = comentario.id
            new_visit.save()
            """
            #Recuperamos todas las visitas, incluída la nueva
            visitas = Visita.objects.filter(paciente_id=paciente.id).order_by('id').reverse()
            #Añadimos los datos al context que sean revelantes para gestor_de_paciente
            context = {'visitas' : visitas, 'visit_success' : True}
            return render(request, 'pages/gestor_de_paciente.html', context)
        else:
            context = {'formVisita' : formVisita, 'formComentario' : formComentario}
            return render(request, 'pages/crear_visita.html', context)
    #Se llega mediante un hiperenlace (/gestor/nss) o porque el formulario no es válido
    
    #Creamos los formularios que se van a usar en crear_visita
    formVisita = VisitaForm(initial = {'paciente': paciente.id}, prefix = 'visita')
    formComentario = ComentarioVisitaForm(initial = {'autor': request.user.first_name +' ' + request.user.last_name}, prefix = 'comentario')
    #Añadimos los formularios al context, solo relevantes para la vista crear_visita
    context = {'formVisita' : formVisita, 'formComentario' : formComentario}
    return render(request, 'pages/crear_visita.html', context)

@login_required
def nuevo_rango(request):
    #Recojo el nss del paciente desde la sesion 
    paciente = PacienteClinica.objects.get(nss=request.session['nss'])

    #¿Se llega aquí desde un formulario con metodo POST?
    if request.method == 'POST':
        # Comprobamos los rangos:
        if request.POST['rango_inf'] < request.POST['rango_sup']:
            #Añadimos el nuevo rango al paciente de la sesion
            paciente.rango_inf = request.POST['rango_inf']
            paciente.rango_sup = request.POST['rango_sup']
            #Actualizamos el paciente en la base de datos
            paciente.save()
            request.session['rango_inf'] = request.POST['rango_inf']
            request.session['rango_sup'] = request.POST['rango_sup']

    return redirect('/gestor/')
        
@login_required
def guias(request):
    return render(request, 'pages/guias.html')


# LLAMADAS AJAX:
@login_required
def mostrar_visita(request):
    id_visita = request.GET.get('id', None)
    visita = Visita.objects.get(id = id_visita)
    data = {'valorINR':visita.valorINR, 'fecha': str(formats.date_format(visita.fecha, "d-m-Y")),
            'dosis':visita.dosis, 'duracion':visita.duracion,
            'peso':visita.peso,
            'medicacion': Medicacion.objects.get(id=visita.medicacion_id).nombre}
    comentarios = Comentario.objects.filter(visita_id = id_visita)
    all_comments = ""
    for comentario in comentarios:
        if comentario.texto is not None:
            all_comments = all_comments + "-" + comentario.texto + "\n"
    data['comentarios']=all_comments
    return JsonResponse(data)
  
@login_required
def asociar_diagnostico(request):
    # Recogemos los datos enviados por GET
    id_paciente = request.GET.get('paciente_id', None)
    diagnostico_id = request.GET.get('diagnostico_id', None)
    # Encontramos el paciente y el diagnostico 
    if id_paciente and diagnostico_id:
        try:
            paciente = PacienteClinica.objects.get(id=id_paciente)
            diagnostico = Diagnostico.objects.get(id=diagnostico_id)
            # Añadimos el diagnóstico a la lista de diagnósticos del paciente
            paciente.diagnosticos.add(diagnostico)
            # Creamos los datos que se van a devolver para crear la nueva fila de la tabla
            data = {'codigo':diagnostico.codigo, 'descripcion':diagnostico.descripcion}
        except DoesNotExist:
            data = {}
    return JsonResponse(data)

@login_required
def anadir_comentario(request):
    id_visita = request.GET.get('id', None)
    nuevo_comentario = request.GET.get('nuevo_comentario', None)
    autor = request.GET.get('autor', None)
    if id_visita and nuevo_comentario and autor:
        comentario = Comentario()
        comentario.visita_id = id_visita
        comentario.texto = nuevo_comentario
        comentario.autor = autor
        comentario.save()

        comentarios = Comentario.objects.filter(visita_id = id_visita)
        all_comments = ""
        for comentario in comentarios:
            if comentario.texto is not None:
                all_comments = all_comments + "-" + comentario.autor + ": " + comentario.texto + "\n --- \n"

        data = {'todos_comentarios': all_comments}

    else:
        data = {}

    return JsonResponse(data)
