from __future__ import unicode_literals

from django.db import models
import uuid


class Comentario(models.Model):
    texto = models.CharField(
        db_column="NSS", max_length=45, blank=True, null=True)


class PacienteClinica(models.Model):
    nss = models.CharField(
        db_column="NSS", max_length=45, blank=True, null=True)
    password = models.CharField(
        db_column='password', max_length=45, blank=False, null=False)
    token = models.CharField(db_column='token', max_length=45,
                             blank=False, null=False, default=uuid.uuid4().hex)
    dni = models.CharField(
        db_column='dni', max_length=45, blank=True, null=False)
    nombre = models.CharField(
        db_column="Nombre", max_length=45, blank=False, null=True)
    apellido_1 = models.CharField(
        db_column="apellido_1", max_length=45, blank=False, null=True)
    apellido_2 = models.CharField(
        db_column="apellido_2", max_length=45, blank=False, null=True)
    cp = models.IntegerField(
        db_column='cp', blank=False, null=True)
    telefono = models.IntegerField(
        db_column='telefono', blank=False, null=True)
    ciudad = models.CharField(
        db_column="ciudad", max_length=45, blank=False, null=True)
    provincia = models.CharField(
        db_column="provincia", max_length=45, blank=False, null=True)
    pais = models.CharField(
        db_column="pais", max_length=45, blank=False, null=True)
    fecha_nacimiento = models.DateField(
        db_column='fecha_nacimiento', null=True)
    sexo_choices = (
        ('0', 'hombre'),
        ('1', 'mujer'),)
    sexo = models.CharField(
        max_length=1, choices=sexo_choices, default='Sin especificar')


class Diagnostico(models.Model):
    idDiagnostico = models.CharField(
        db_column="idDiagnostico", max_length=45, blank=False, null=False, primary_key=True)
    nombre = models.CharField(
        db_column="Nombre", max_length=45, blank=False, null=True)
    paciente = models.ForeignKey(PacienteClinica)


class Medicacion(models.Model):
    nombre = models.CharField(
        db_column="Nombre", max_length=45, blank=True, null=True)


class Visita(models.Model):
    fecha = models.DateField()
    valorINR = models.DecimalField(
        db_column="valorINR", max_digits=20, decimal_places=10)
    dosis = models.DecimalField(
        db_column="dosis", max_digits=20, decimal_places=10)
    duracion = models.CharField(
        db_column="duracion", max_length=45, blank=True, null=True)
    peso = models.DecimalField(
        db_column="peso", max_digits=20, decimal_places=10)
    rango = models.CharField(
        db_column="rango", max_length=45, blank=True, null=True)
    paciente = models.ForeignKey(PacienteClinica, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    medicacion = models.ForeignKey(Medicacion, on_delete=models.CASCADE)
