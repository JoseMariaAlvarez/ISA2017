>Esta pequeña guía se basa en el contenido de:
tutorial.djangogirls.org/es/,
effectivedjango.com/tutorial/index.html,
librosweb.es/libro/django_1_0/
y
djangotutorial.readthedocs.io/es/1.8/intro/overview.html

Damos por hecho que estamos trabajando en un **entorno virtual**.

 ----------

# Inicialización
Para crear el proyecto crearemos una carpeta llamada *proyecto* y, una vez dentro, y ejecutaremos:
```python
$ django-admin startproject mysite .
```
> El punto al final le dice a Django que cree el proyecto en el directorio actual.

Se creará la siguiente estructura de carpetas:
```
proyecto
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
Modificaremos el archivo *proyecto/mysite/settings.py* para especificar la ruta de los archivos estáticos (lo veremos más adelante) añadiendo debajo de `STATIC_URL`:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

# Base de datos
Por defecto, la configuración usa SQLite como sistema de base de datos. Esta es la opción más simple para pruebas locales.

Para crear la base de datos, vamos a la carpeta *proyecto* y ejecutamos:
```python
$ python manage.py migrate
```

Para iniciar el servidor en la dirección local http://127.0.0.1:8000/ usamos:
```python
$ python manage.py runserver
```

# Crear aplicaciones
Para crear una aplicación, ejecutamos:
```python
$ python manage.py startapp blog
```
La nueva estructura de nuestro proyecto será:
```
proyecto
├── mysite
|       __init__.py
|       settings.py
|       urls.py
|       wsgi.py
├── manage.py
└── blog
    ├── migrations
    |       __init__.py
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── tests.py
    └── views.py
```
Debemos decirle a Django que use la app. Para ello, añadimos al campo `INSTALLED_APPS` del archivo *proyecto/mysite/settings.py* la siguiente línea de código:
```python
INSTALLED_APPS = (
    ...
    'blog',
)
```

# Modelos
Los modelos servirán como el esquema de nuestra base de datos. Para crearlos, modificamos el archivo *proyecto/blog/models.py* añadiendo al final:
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(
        max_length=15 )
    apellidos = models.CharField(
        max_length=15 )
    email = models.EmailField()

    def __unicode__(self): # __str__ en Python 3.X
        return ' '.join([
            self.nombre,
            self.apellidos,
        ])

class Empresa(models.Model):
    empresa = models.CharField(
        max_length=15 )
    contacto = models.ForeignKey(Contacto, null=True, blank=True, default=None, on_delete=models.CASCADE)

    def __unicode__(self): # __str__ en Python 3.X
        return self.empresa

```

>`models.ForeignKey()` define una relación 1:n; `models.ManyToMany()` sirve para definir una relación m:n; `models.OneToOneField` sirve para definir una relación 1:1.

En este caso estamos creando un modelo Contacto, que tendrá un nombre, apellidos e email. La utilidad del método `def __unicode__(self)` la veremos más adelante.

### Cambios en la base de datos
De ahora en adelante, siempre que modifiquemos el modelo, para que Django sepa que hemos hecho cambios (en este caso, crearlo), ejecutaremos:
```python
$ python manage.py makemigrations blog
```
Y lo aplicamos a la base de datos escribiendo:
```python
$ python manage.py migrate blog
```

# Interactuar con la base de datos
### Administrador.
Para agregar, editar o borrar los campos del modelo usando el administrador de Django (http://127.0.0.1:8000/admin/), vamos a *proyecto/blog/admin.py* y añadimos:
```python
from .models import Contacto, Empresa
admin.site.register(Contacto)
admin.site.register(Empresa)
```
>**Nota:** Para ingresar a http://127.0.0.1:8000/admin/ primero debemos crear un superusuario:
> `$ python manage.py createsuperuser`

Desde el panel de administración crearemos un nuevo contacto rellenando los tres campos y una empresa con un nombre pero *sin* contacto asociado. Lo usaremos como ejemplo en el siguiente punto.

### Shell.
Django nos ofrece una API Python para trabajar con estos modelos sin necesidad de usar el administrador. Para ello, ejecutamos:
```python
python manage.py shell
```
Desde ahí ejecutaremos la siguiente secuencia de comandos:
```python
$ from blog.models import Contacto, Empresa
$ c1 = Contacto(nombre="Marco", apellidos="Sánchez Sánchez", email="marco@sanchez.com")
$ c1.save()
$ em = Empresa(empresa="Indr", contacto=c1)
$ em.save()
$ lista_contactos = Contacto.objects.all()
$ lista_contactos
<QuerySet [<Contacto: Luis Ruíz Torres>, <Contacto: Marco Sánchez Sánchez>]>
```
Como vemos, `lista_contactos` nos devuelve todos los contactos escribiendo el nombre y los apellidos. Si a la hora de crear el modelo Contacto no hubiésemos creado el método `def __unicode__(self)`, veríamos:
```python
<QuerySet [<Contacto: Contacto object>, <Contacto: Contacto object>]>
```
Además, podemos ver que para guardar el objeto en la base de datos hay que llamar al método `save()` (con esto Django realiza una sentencia `INSERT` de SQL).

# Vistas
Las vistas nos permiten, dada una petición, devolver una respuesta web. Estas vistas puede leer registros de una base de datos, o no. Puede usar un sistema de templates como el de Django – o algún otro basado en Python –, o no. Puede generar un archivo PDF, una salida XML, crear un archivo ZIP, cualquier cosa que uno quiera, usando cualquier librería Python que uno quiera.

Para crearlas, vamos a *proyecto/blog/views.py* y añadimos:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
```
Esta es la vista más simple que podemos crear. Devuelve una respuesta.

También podríamos incluir código HTML en la respuesta. Por ejemplo:
```python
def index(request):
    time_now = datetime.datetime.now()
    html = "<p>Hora: %s.</p>" % time_now
    return HttpResponse(html)
```
Esto no es una buena práctica porque implicaría cambiar el código para cambiar el diseño. Como veremos más adelante, el diseño se hará utilizando un sistema de plantillas.

 Para que la vista cumpla su función necesitamos *mapearla* a una URL. Abrimos *proyecto/mysite/urls.py* y lo cambiamos por:
```python
from django.conf.urls import url
from django.contrib import admin
import blog.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', blog.views.index),
]
```

>Django usa Regex (o expresiones regulares) para definir el string que será la URL (por ejemplo, '^admin/').

Si iniciamos el servidor y vamos a http://127.0.0.1:8000/blog/ veremos el mensaje *Hello world!*.

# Datos dinámicos
### Plantillas
Vamos a usar el sistema de plantillas de Django para separar el diseño de Python mediante la creación de una plantilla que la vista pueda utilizar.

La configuración de `TEMPLATES` del proyecto (*proyecto/mysite/settings.py*) describe cómo Django cargará y creará las plantillas.

En este caso, por defecto, tendremos el atributo `'APP_DIRS':` asignado como  `True`. Así, Django buscará por un subdirectorio *templates* en cada una de las aplicaciones en `INSTALLED_APPS`.

>Django permite usar dos sintaxis diferentes para mostrar datos en las plantillas. Estos dos sistemas (llamados *template engine*) son DTL y Jinja2. Podemos especificar qué sistema usar para cada archivo HTML editando el archivo *settings* y modificando el campo por `'BACKEND':` por `'django.template.backends.django.DjangoTemplates'` o `'django.template.backends.jinja2.Jinja2'`
>
>**Nota:** Para usar Jinja2 debemos instalarlo:
>`$ pip install Jinja2`

Por lo tanto, crearemos una carpeta *templates* dentro de *proyecto/blog/*. Dentro de ella crearemos un archivo llamado *contacts.html* con el siguiente código:
```HTML
<h1>Lista de contactos</h1>
<ul>
  {% for empresa in empresas %}
    {# Esto es un comentario #}
    <div class="well well-lg">
      <li>Empresa: {{ empresa.empresa }}</li>
      {% if empresa.contacto %}
      <li>Nombre: {{ empresa.contacto.nombre }}</li>
      <li>Apellidos: {{ empresa.contacto.apellidos }}</li>
      {% else %}
      <li>No hay contacto.</li>
      {% endif %}
    </div>
  {% endfor %}
</ul>
```
Ya tenemos la plantilla creada. No es más que código HTML con código intercalado. Como podemos ver:
- `{# <texto> #}` añade comentarios,
- `{% <texto> %}` añade funciones propias de Python,
- `{ <texto> }` nos permite acceder a variables.

>Hay más etiquetas y filtros (por ejemplo, `{{ name|lower }}` aplica el filtro `lower` a la variable `name`) disponibles. Puedes consultar la lista completa en la documentación de Django.

Ahora debemos asociarla al modelo usando la vista.

Modificaremos el archivo *proyecto/blog/views.py* y añadiremos:
```python
from blog.models import Empresa
from django.shortcuts import render_to_response

def index(request):
    empresas = Empresa.objects.all()
    template_name = 'contacts.html'

    return render_to_response(template_name, {'empresas': empresas})
```
Esto nos mostrará el nombre de todas las empresas junto al contacto que tenga asociado.

### Bootstrap
*Bootstrap* es un framework para desarrollar páginas web *mobile-first* con diseño adaptables.
Vamos a cambiar nuestra plantilla para hacer uso de Bootstrap: editamos *proyecto/mysite/blog/templates/contacts.html* y ponemos:
```HTML
<!DOCTYPE html>
<head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  <title>Blog - Lista de contactos</title>
</head>

<body>

  <div class="panel panel-default">
    <div class="panel-heading"><h1>Lista de contactos</h1></div>
    <div class="panel-body">
      <ul>
        {% for empresa in empresas %}
          {# Esto es un comentario #}
          <div class="well well-lg">
            <li>Empresa: {{ empresa.empresa }}</li>
            {% if empresa.contacto %}
            <li>Nombre: {{ empresa.contacto.nombre }}</li>
            <li>Apellidos: {{ empresa.contacto.apellidos }}</li>
            {% else %}
            <li>No hay contacto.</li>
            {% endif %}
          </div>
        {% endfor %}
      </ul>
    </div>
  </div>

</body>
```
Como vemos, hemos incluido el contenido que ya teníamos dentro de `<body></body>` y en la cabecera (dentro de `<head></head>`) hemos añadido los enlaces necesarios para incluir Bootstrap a nuestra plantilla.
Además hemos hecho algunos cambios a nuestra lista de contactos: por ejemplo, ahora la lista con *Nombre* y *Apellidos* ahora están dentro de `<div class="well well-lg"></div>`. El campo `class` especifica qué tipo de componente es.

Puedes ver la lista completa de componentes en la documentación oficial de Bootstrap.

### Bloques
Cuando creemos nuestra página web puede que queramos que todas las páginas  cuenten con la misma cabecera, pie de página y, quizá, otros elementos en común. Para ello podemos crear una plantilla *base* que cuente con todos los elementos comunes y haremos que nuestras plantillas extiendan de la plantilla base.

Crearemos dentro de *proyecto/blog/templates/* un archivo *base.html* con el siguiente contenido:
```HTML
<!DOCTYPE html>
<head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  <title>Blog - {% block title %}{% endblock %}</title>
</head>

<body>
  {% block body_block %}
  {% endblock %}
</body>
```

...y modificaremos *contacts.html* para que se parezca a:
```HTML
{% extends 'base.html' %}

{% block title %}Lista de contactos{% endblock %}

{% block body_block %}
  <div class="panel panel-default">
    <div class="panel-heading"><h1>Lista de contactos</h1></div>
    <div class="panel-body">
      <ul>
        {% for empresa in empresas %}
          {# Esto es un comentario #}
          <div class="well well-lg">
            <li>Empresa: {{ empresa.empresa }}</li>
            {% if empresa.contacto %}
            <li>Nombre: {{ empresa.contacto.nombre }}</li>
            <li>Apellidos: {{ empresa.contacto.apellidos }}</li>
            {% else %}
            <li>No hay contacto.</li>
            {% endif %}
          </div>
        {% endfor %}
      </ul>
    </div>
  </div>
{% endblock %}
```

Como vemos, hemos creado bloques para especificar el contenido de cada sección de *base.html*.

### Ficheros estáticos
Al principio de esta guia modificamos el archivo *proyecto/mysite/settings.py* para especificar la ruta de los archivos estáticos.

Los archivos estáticos serán todas los ficheros que no se van a modificar, como archivos *.css*, códigos *.js* o imágenes de fondo, cabecera... En nuestro ejemplo anterior añadimos en el `<head></head>`:
```HTML
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
```
Podríamos guardar la hoja de estilo en nuestra página web en una carpeta estática para hacer referencia a ella en lugar de usar un hiperenlace.
Para ello, crearemos una carpeta en *proyecto/blog/* llamada *static* (al igual que creamos *templates*) y, en ella, crearemos una carpeta *css* e incluiremos dentro nuestro fichero *bootstrap.min.css*.

Modificaremos la plantilla *base.html* para hacer referencia a estos ficheros estáticos:
```HTML
<head>
  {% load staticfiles %}
  <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  <link rel="stylesheet" type="text/css" href="{% static '/css/bootstrap.min.css' %}" />
  <title>Blog - {% block title %}{% endblock %}</title>
</head>
```
