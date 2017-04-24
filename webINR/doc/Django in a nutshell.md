>Esta pequeña guía se basa en el contenido de:
https://tutorial.djangogirls.org/es/,
http://www.effectivedjango.com/tutorial/index.html
y
http://djangotutorial.readthedocs.io/es/1.8/intro/overview.html

Damos por hecho que estamos trabajando en un **entorno virtual**.

 ----------

# Inicialización
Para crear el proyecto, crearemos una carpeta llamada *proyecto* y, una vez dentro, y ejecutaremos:
```python
$ django-admin startproject mysite .
```
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
Por defecto, la configuración usa SQLite. Está es la opción más simple para pruebas locales.
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

### Modelos
Los modelos servirán como el esquema de nuestra base de datos. Para crearlos, modificamos el archivo *proyecto/blog/models.py* añadiendo al final:
```python
class Contacto(models.Model):
    nombre = models.CharField(
        max_length=255, )
    apellidos = models.CharField(
        max_length=255, )
    email = models.EmailField()

    def __str__(self):
        return ' '.join([
            self.nombre,
            self.apellidos,
        ])
```
En este caso estamos creando un modelo Contacto, que tendrá un nombre, apellidos e email.

# Cambios en la base de datos
De ahora en adelante, siempre que modifiquemos el modelo, para que Django sepa que hemos hecho cambios (en este caso, crearlo), ejecutaremos:
```python
$ python manage.py makemigrations blog
```
Y lo aplicamos a la base de datos escribiendo:
```python
$ python manage.py migrate blog
```

# Administrador de Django
Para agregar, editar o borrar los campos del modelo usando el administrador de Django (http://127.0.0.1:8000/admin/), vamos a *proyecto/blog/admin.py* y añadimos:
```python
from .models import Contacto
admin.site.register(Contacto)
```
>**Nota:** Para ingresar a http://127.0.0.1:8000/admin/ primero debemos crear un superusuario:
> `$ python manage.py createsuperuser`

Desde el panel de administración, vamos a crear un nuevo contacto rellenando los tres campos. Lo usaremos en el siguiente punto.

### Shell.
Django nos ofrece una API Python para trabajar con estos modelos sin necesidad de usar el administrador. Para ello, ejecutamos:
```python
python manage.py shell
```
Desde ahí ejecutaremos la siguiente secuencia de comandos:
```
$ from blog.models import Contacto
$ c1 = Contacto(nombre="Marco", apellidos="Sánchez Sánchez", email="marco@sanchez.com")
$ c1.save()
$ lista_contactos = Contacto.objects.all()
$ lista_contactos
<QuerySet [<Contacto: Luis Ruíz Torres>, <Contacto: Marco Sánchez Sánchez>]>
```
Como vemos, `lista_contactos` nos devuelve todos los contactos escribiendo el nombre y los apellidos. Si a la hora de crear el modelo Contacto no hubiésemos creado el método `__str__`, veríamos:
```python
<QuerySet [<Contacto: Contacto object>, <Contacto: Contacto object>]>
```
Además, para guardar el objeto en la base de datos debemos llamar al método `save()` (con esto Django realiza una sentencia `INSERT` de SQL).


# Vistas
Las vistas nos permiten, dada una petición, devolver una respuesta web. Estas vistas puede leer registros de una base de datos, o no. Puede usar un sistema de templates como el de Django – o algún otro basado en Python –, o no. Puede generar un archivo PDF, una salida XML, crear un archivo ZIP, cualquier cosa que uno quiera, usando cualquier librería Python que uno quiera.

Para crearlas, vamos a *blog/views.py* y añadimos:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
```
Esta es la vista más simple que podemos crear. Devuelve una respuesta HTML. Para que la vista cumpla su función necesitamos *mapearla* a una URL. Abrimos *proyecto/mysite/urls.py* y lo cambiamos por:
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
Para ello crearemos una carpeta *templates* dentro de *proyecto/blog/*.

La configuración de `TEMPLATES` del proyecto (*proyecto/mysite/settings.py*) describe cómo Django cargará y creará las plantillas.

En este caso, por defecto, tendremos el atributo `'APP_DIRS':` asignado como  `True`. Así, Django buscará por un subdirectorio *templates* en cada una de las aplicaciones en `INSTALLED_APPS`.

>Django permite usar dos sintaxis diferentes para mostrar datos en las plantillas. Estos dos sistemas (llamados *template engine*) son DTL y Jinja2. Podemos especificar qué sistema usar para cada archivo HTML editando el archivo *settings* y modificando el campo por `'BACKEND':` por `'django.template.backends.django.DjangoTemplates'` o `'django.template.backends.jinja2.Jinja2'`
>
>**Nota:** Para usar Jinja2 debemos instalarlo:
>`$ pip install Jinja2`

Dentro de *templates* crearemos un archivo llamado *contacts.html* con el siguiente código:
```HTML
<h1>Lista de contactos</h1>
<ul>
  {% for contacto in lista_contactos %}
    {# Esto es un comentario #}
    <li>Nombre: {{ contacto.nombre }}</li>
    <li>Apellidos: {{ contacto.apellidos }}</li>
  {% endfor %}
</ul>
```
Ya tenemos la plantilla creada. Ahora debemos asociarla al modelo usando la vista.

Modificaremos el archivo *proyecto/blog/views.py* y añadiremos:
```python
from blog.models import Contacto
from django.shortcuts import render_to_response

def index(request):
    lista_contactos = Contacto.objects.all()
    template_name = 'contacts.html'

    return render(template_name, {'lista_contactos': lista_contactos})
```
Esto nos mostrará el nombre y apellido de todos los contactos en la base de datos.

### Formularios
>// TODO
