# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Medicación Adicional
class Medicacion_adicional(models.Model):
    nombre = models.CharField(
        db_column='nombre', max_length=255, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.nombre)

# Diagnostico model
class Diagnostico(models.Model):
    codigo = models.CharField(
        db_column="codigo", max_length=7, blank=False, null=False, unique=True)
    descripcion = models.CharField(
        db_column="descripcion", max_length=255, blank=False, null=True)

# Medicacion model
class Medicacion(models.Model):
    nombre = models.CharField(
        db_column="Nombre", max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre

# PacienteClinica model
class PacienteClinica(models.Model):
    nss = models.CharField(
        db_column="NSS", max_length=45, blank=True, null=True, unique=True)
    password = models.CharField(
        db_column='password', max_length=45, blank=False, null=False, default=uuid.uuid4().hex)
    token = models.CharField(db_column='token', max_length=45,
                             blank=False, null=False, default=uuid.uuid4().hex)
    dni = models.CharField(
        db_column='dni', max_length=45, blank=True, null=False, unique=True)
    nombre = models.CharField(
        db_column="Nombre", max_length=45, blank=False, null=True)
    apellido_1 = models.CharField(
        db_column="apellido_1", max_length=45, blank=False, null=True)
    apellido_2 = models.CharField(
        db_column="apellido_2", max_length=45, blank=False, null=True)
    direccion = models.CharField(
        db_column="direccion", max_length=90, blank=False, null=True)
    cp = models.IntegerField(
        db_column='cp', blank=False, null=True)
    telefono = models.IntegerField(
        db_column='telefono', blank=False, null=True, unique=True)
    ciudad = models.CharField(
        db_column="ciudad", max_length=45, blank=False, null=True)
    provincia = models.CharField(
        db_column="provincia", max_length=45, blank=False, null=True)
    pais = models.CharField(
        db_column="pais", max_length=45, blank=False, null=True)
    fecha_nacimiento = models.DateField(
        db_column='fecha_nacimiento', null=True)
    rango = models.CharField(
        db_column="rango", max_length=45, blank=True, null=True)
    sexo_choices = (
        ('0', 'hombre'),
        ('1', 'mujer'),)
    sexo = models.CharField(
        max_length=1, choices=sexo_choices, default='1')
    diagnosticos = models.ManyToManyField(Diagnostico)
    medicaciones_adicionales = models.ManyToManyField(Medicacion_adicional)

    def __str__(self):
        return '%s - %s %s' % (self.dni, self.nombre, self.apellido_1)

# Visita model
class Visita(models.Model):
    fecha = models.DateField()
    valorINR = models.DecimalField(
        db_column="valorINR", max_digits=2, decimal_places=1)
    dosis = models.DecimalField(
        db_column="dosis", max_digits=5, decimal_places=2)
    duracion = models.CharField(
        db_column="duracion", max_length=45, blank=True, null=True)
    peso = models.DecimalField(
        db_column="peso", max_digits=5, decimal_places=2)
    paciente = models.ForeignKey(PacienteClinica, on_delete=models.CASCADE)
    medicacion = models.ForeignKey(Medicacion, on_delete=models.CASCADE)

# Comentario model
class Comentario(models.Model):
    texto = models.CharField(
        db_column="text", max_length=255, blank=True, null=True)
    visita = models.ForeignKey(Visita)
    autor = models.CharField(
        db_column="autor", max_length=45, blank=False, null=False, default='-')
    def __str__(self):
        return '%s' % self.texto
