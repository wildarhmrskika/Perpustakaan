from flask import Flask, render_template, request, url_for, redirect
from konsepOOP import DatabaseManager, Buku, KelolaBuku, User
import sqlite3

app = Flask('__name__')

db_manager = DatabaseManager("db_belajar_jalan.db")
semua_buku = KelolaBuku("db_belajar_jalan.db")


@app.route('/', methods=['GET', 'POST'])
def index():

    tagar = db_manager.execute_query("SELECT * FROM tagar").fetchall()

    if request.method == 'GET':
        data_buku = semua_buku.tampilkan_buku()
        return render_template('index.html', data_buku=data_buku,	tagar=tagar)
    elif request.method == 'POST':
        search_value = request.form.get("search")
        buku = semua_buku.cari_buku(search_value)
        if (buku):
            return render_template('cari.html', data_buku=buku)
        else:
            return render_template('notfound.html')


@app.route('/tambah_buku', methods=['GET', 'POST'])
def tambah_buku():

    if request.method == 'GET':
        return render_template('tambah_buku.html')
    elif request.method == 'POST':

        judul = request.form.get('judul')
        kategori = request.form.get('kategori')
        deskripsi = request.form.get('deskripsi')
        file = request.files['file']
        sampul = request.files['sampul']

        buku_baru = Buku("db_belajar_jalan.db", judul, kategori,
                         deskripsi, file.filename, sampul.filename)
        buku_baru.tambah_data()

        file.save('static/pdf/'+file.filename)
        sampul.save('static/img/'+sampul.filename)

        if buku_baru:
            return redirect(url_for('index'))
        else:
            return 'gagal'


@app.route('/admin', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('pass')

        user = User("db_belajar_jalan.db", username, password)
        if user.cek_user() == '200':
            return redirect(url_for('tambah_buku'))
        else:
            return render_template('login.html')

@app.route('/daftar', methods=['POST', 'GET'])
def daftar():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'GET':
        return render_template('daftar.html')
    else:
        user = User("db_belajar_jalan.db", username, password)
        user.tambah_data()
        if (user):
            return 'berhasil terdaftar'
        else:
            return 'tidak berhasil'


@app.route('/baca/<int:id_buku>')
def baca(id_buku):
    buku = semua_buku.baca_buku(id_buku)
    return render_template('read.html', buku=buku)


@app.route('/tags/<kategori>', methods=['GET', 'POST'])
def cari_buku_kategori(kategori):
    if request.method == "GET":
        buku = semua_buku.tampil_berdasarkan_kategori(kategori)
        return render_template('tags.html', buku=buku)
    elif request.method == 'POST':
        search_value = request.form.get("search")
        buku = semua_buku.cari_buku(search_value)
        if (buku):
            return render_template('cari.html', data_buku=buku)
        else:
            return render_template('notfound.html')


if __name__ == '__main__':
    app.run(debug=True)


@app.teardown_appcontext
def close_db_connection(exception=None):
    db_manager.close_connection()
