from django.contrib.auth.models import User
from MySQLDriver import MySQLConn


class LoginBackend(object):

    def authenticate(self, request, username=None, password=None):
        try:
            connection = MySQLConn(
                database="usuariossanitarios", username='root', password='root')
            cursor = connection.cursor

            query = ('SELECT usuario, password, nombre, apellido1 FROM usuarios_sanitarios WHERE usuario="?" AND password="?"',(
                request.POST['username'], request.POST['password']))
            cursor.execute(query)
            for usuario, password, nombre, apellido1 in cursor:
                u, c = User.objects.get_or_create(
                    username=usuario, password=password, first_name=nombre, last_name=apellido1)
        except User.DoesNotExist:
            return None
        return u

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
