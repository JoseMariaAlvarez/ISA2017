import mysql.connector

class MySQLConn:
	def __init__(self, database, username, password):
		self.database = database
		self.username = username
		self.password = password
		try:
			self.cnx = mysql.connector.connect(user=username, password=password, database=database)
		except Exception as e:
			raise e

	@property
	def cursor(self):
		return self.cnx.cursor()
