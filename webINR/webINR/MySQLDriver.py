import mysql.connector

"""Driver for MySQL connections, currently supporting a cursor
    to operate with the object. The connection object must be either 
    closed or destroyed. """ 

class MySQLConn:

    def __init__(self, database, username, password, host, port=3306):
        self.database = database
        self.username = username
        self.password = password
        self.host = host
        self.port = port

        try:
            self.cnx = mysql.connector.connect(
                user=username, password=password, database=database, host=host, port=port)
        except Exception as e:
            raise e

    @property
    def cursor(self):
        return self.cnx.cursor()
