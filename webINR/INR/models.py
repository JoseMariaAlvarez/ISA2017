from __future__ import unicode_literals

from django.db import models

class Comentario(models.Model):
	texto = models.CharField(
		db_column="NSS", max_length=45, blank=True, null=True)

class PacienteClinica(models.Model):
	nss = models.CharField(
		db_column="NSS", max_length=45, blank=True, null=True)

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