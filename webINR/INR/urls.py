from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ficha/$', views.ver_ficha, name='ficha'),
    url(r'^alta/$', views.dar_alta, name='alta'),
    url(r'^buscar/$', views.buscar, name='busqueda'),
]
