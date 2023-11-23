from flask import Flask, render_template, request, url_for, redirect
import sqlite3 
from konsepOOP import *

app = Flask('__name__') 


conn = sqlite3.connect('test.db',check_same_thread=False)

@app.route('/', methods = ['GET', 'POST'])
def index():
	cur = conn.cursor()
	data = cur.execute('select * from buku').fetchall()

	a = tagar().fetchA()
	if request.method == 'GET':
		print(a)
		return render_template('index.html', data=data,	a=a)
	elif request.method == 'POST':
		search = cur.execute('select * from buku where LOWER(judul)=LOWER("{}")'.format(request.form.get('ok'))).fetchall()	
		if(search):
			return render_template('cari.html', hebat=search)
		else:
			return render_template('notfound.html')
@app.route('/dash', methods = ['GET','POST'])
def dash():
	ok = ""
	Aj = request.form.get('judul')
	Ak = request.form.get('kategori')
	Ad = request.form.get('deskripsi')
	Af = request.form.get('file')
	As = Aj = request.form.get('sampul')
	if request.method == 'GET':
		return render_template('info.html', ok=ok)
	else:
		# curs = conn.cursor()
		# cek = curs.execute(f"insert into buku values (null,'{Aj}','{Ak}','{Ad}','{Af}','{As}')")
		# conn.commit()
		return 'pl'

		if cek:
			return redirect(url_for('index'))
		else:
			return 'gagal'

@app.route('/admin', methods = ['GET', 'POST'])
def login():
	user = request.form.get('user')
	pw = request.form.get('pass')
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		l = Login(user,pw)
		if l.Check() == '200':
			return redirect(url_for('dash'))
		else:
			return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)