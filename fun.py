import sqlite3 

class FetchDb:
	def __init__(self):
		self.conn = sqlite3.connect('test.db')

	def fetchA(self):
		data = self.conn.execute('select * from terbaru').fetchall()
		return data

class tagar(FetchDb):
	def fetchA(self):
		data = self.conn.execute('select * from tagar').fetchall()
		return data
		
class Login:

	def __init__(self,user,pword):
		self.user = user
		self.__pasw = pword

	def Check(self):
		if self.user == 'admin':
			if self.__pasw == '123':
				print('OK')
				return '200'
		else :
			print('ok')
			return '404'