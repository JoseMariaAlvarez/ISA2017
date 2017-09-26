from django.test import TestCase
from django.db import IntegrityError
from .models import PacienteClinica, Medicacion
from .forms import AltaForm

class BDTest(TestCase):
    def create_patient(self):
        return PacienteClinica(
            nss='1234', password='p1', dni='123A',nombre='person1',
            apellido_1='s1',apellido_2='s2',direccion='c/etc',cp='2009',
            telefono='65000001',ciudad='MAL',provincia='MAL',pais='MAL',
            fecha_nacimiento='2001-01-01',rango_inf='2.3',rango_sup='3.9',sexo=0)

    def test_valid_form_alta(self):
        p1 = self.create_patient()
        p1.save()

        data = {'dato': p1.nss}
        form = AltaForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form_alta_charfield_too_big(self):
        data = {'dato': '123456789012345678901234567890'}
        form = AltaForm(data=data)

        self.assertFalse(form.is_valid())

    def test_patient_isinstance(self):
        p1 = self.create_patient()

        self.assertTrue(isinstance(p1, PacienteClinica))
'''
    def test_unique_person_constrain(self):
        p1 = self.create_patient()
        p1.save()

        p2 = self.create_patient()

        self.assertRaises(IntegrityError, p2.save())
'''