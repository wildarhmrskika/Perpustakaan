import sqlite3 

class FetchDb:
	def __init__(self):
		self.conn = sqlite3.connect('test.db')

	def fetchA(self):
		data = self.conn.execute('select * from terbaru').fetchall()
		self.conn.close()
		return data

class tagar(FetchDb):
	def fetchA(self):
		data = self.conn.execute('select * from tagar').fetchall()
		self.conn.close()
		return data

class Hebat(FetchDb):
	def __init__ (self,judul,kategori,deskripsi,file,sampul):
		self.judul = judul
		self.kategori = kategori
		self.deskripsi = deskripsi
		self.file = file
		self.sampul = sampul
	def insertData(self):
		sen = self.conn.execute(f"insert into terbaru values(null,'{self.judul},{self.kategori},{self.deskripsi},{self.file},{self.sampul}')")
		if sen:
			code = 200
			return 'ok'
		else:
			code = 404
			return 'no'
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