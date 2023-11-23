from flask import Flask, render_template, request
import sqlite3 
from konsepOOP import *

app = Flask('__name__') 

@app.route('/', methods = ['GET', 'POST'])
def index():
	conn = sqlite3.connect('test.db')
	cur = conn.cursor()
	data = cur.execute('select * from terbaru').fetchall()

	a = tagar().fetchA()
	if request.method == 'GET':
		print(a)
		return render_template('index.html', data=data,	a=a)
	elif request.method == 'POST':
		search = cur.execute('select * from terbaru where LOWER(judul)=LOWER("{}")'.format(request.form.get('ok'))).fetchall()	
		if(search):
			return render_template('cari.html', hebat=search)
		else:
			return render_template('notfound.html')

@app.route('/admin', methods = ['GET', 'POST'])
def login():
	user = request.form.get('user')
	pw = request.form.get('pass')
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		l = Login(user,pw)
		if l.Check() == '200':
			b = request.form.get('judul')
			c = request.form.get('kategori')
			d = request.form.get('deskripsi')
			e = request.form.get('file')
			g = request.form.get('sampul')
			return render_template('info.html')
			i = hebat(b,c,d,e,g)
			keren = i.insertData()
			if keren:
				return b,c,d,e,g
			else:
				return 'not ok'
		else:
			return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)