import MySQLdb


class MySQLConn:

    def __init__(self, database, username, password, host, port=3306):
        self.database = database
        self.username = username
        self.password = password
        self.host = host
        self.port = port

        try:
            self.cnx = MySQLdb.connect(
                user=username, passwd=password, db=database, host=host, port=port)
        except Exception as e:
            raise e

    @property
    def cursor(self):
        return self.cnx.cursor()
