# -*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views

""" Accessible URL patterns.
    * ficha/
    * alta/
    * buscar/
    * visitas/<nss>
    * modvisitas/<id>
    * datos_paciente/<nss>
"""

## Las URL nos permiten acceder a las vistas desde un patrón concreto
## Así, al acceder a /ficha/, estaré accediendo a la vista 'ver_ficha'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ficha/$', views.ver_ficha, name='ficha'),
    url(r'^alta/$', views.dar_alta, name='alta'),
    url(r'^buscar/$', views.buscar, name='busqueda'),
    url(r'^modvisitas/(?P<id>\w{0,50})/$', views.cambiar_visita, name='modvisitas'),
    url(r'^crearvisita/(?P<nss>\w{0,50})/$', views.crear_visita, name='crearvisita'),
]
