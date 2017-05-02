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
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ficha/$', views.ver_ficha, name='ficha'),
    url(r'^alta/$', views.dar_alta, name='alta'),
    url(r'^buscar/$', views.buscar, name='busqueda'),
    url(r'^visitas/(?P<nss>\w{0,50})/$', views.get_visitas, name='visita'),
    url(r'^modvisitas/(?P<id>\w{0,50})/$', views.cambiar_visita, name='modvisitas'),
    url(r'^datos_paciente/(?P<nss>\w{0,50})/$', views.get_datos_demograficos, name='datos_paciente'),
]
