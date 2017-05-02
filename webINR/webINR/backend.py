# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from MySQLDriver import MySQLConn

""" Docstring for custom backend. (https://docs.djangoproject.com/en/1.11/topics/auth/customizing/)
    Authenticate and get_user methods are overriden to match the login requirements
    of this application. It asks a remote database for the information (Username, Password)
    and acts in consequence """

class LoginBackend(object):

    def authenticate(self, request, username=None, password=None):
        try:
            ## Establecemos conexión con la base de datos
            connection = MySQLConn(
                host="localhost", database="usuariossanitarios", username='root', password='root', port=3306)
            cursor = connection.cursor

            ## Establecemos y ejecutamos nuestra query
            query = 'SELECT usuario, password, nombre, apellido1 FROM usuarios_sanitarios WHERE usuario="%s" AND password="%s"' % (
                request.POST['username'], request.POST['password'])
            cursor.execute(query)

            user = None

            for usuario, password, nombre, apellido1 in cursor:
                user = User.objects.get_or_create(
                    username=usuario, password=password, first_name=nombre, last_name=apellido1)[0]
            return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
