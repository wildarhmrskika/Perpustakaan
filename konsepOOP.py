import sqlite3

#PUTRI ANGRAINI AZIZ
# mama induk #
class DatabaseManager:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        conn = sqlite3.connect(
            db_file, check_same_thread=False, isolation_level=None)
        return conn

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        return cursor

# ROSALINA
# inherintes 
# kaerana dia mewarisi sifat dari induknya yaitu datebasemanajer #
class Buku(DatabaseManager):
    def __init__(self, db_file, judul, kategori, deskripsi, file, sampul):
        #super init dia pemanggilan konstruktor dari kelas induk , jadi super init  berguna ketika kelas anak memiliki konstruktor 
        #sendiri dan ingin mengeksekusi konstruktor kelas induk juga #
        super().__init__(db_file)
        self.judul = judul
        self.kategori = kategori
        self.deskripsi = deskripsi
        self.file = file
        self.sampul = sampul

    def tambah_data(self):
        query = f"INSERT INTO terbaru VALUES (null, '{self.judul}', '{self.kategori}', '{self.deskripsi}', '{self.file}', '{self.sampul}')"
        self.execute_query(query)

#WILDA 
class KelolaBuku(DatabaseManager):
    def tampilkan_buku(self):
        query = "SELECT * FROM terbaru"
        return self.execute_query(query).fetchall()

    def tampil_berdasarkan_kategori(self, kategori):
        query = f"SELECT * FROM terbaru WHERE kategori = '{kategori}'"
        return self.execute_query(query).fetchall()

    def cari_buku(self, search_value):
        query = f"SELECT * FROM terbaru WHERE judul LIKE '%{search_value}%'"
        return self.execute_query(query).fetchall()

    def baca_buku(self, id_buku):
        query = f'select * from terbaru where id={id_buku}'
        return self.execute_query(query).fetchall()

# RAHMA DAMAYANTI

class User(DatabaseManager):
    def __init__(self, db_file, username, password):
        super().__init__(db_file)
        self.username = username
        self.__password = password
        # ini merupakan konsep engkapsulesain atau pembungkusan karena password ini sifanya privat bisa di lihat dari kodenya 
        # jadi password ini hanya bisa digunakan di kelas user tidak bisa digunakan di kelas lain ketika kita menggunakan
        # password di kelas lain tidak akan bisa
         8

    def tambah_data(self):
        query = f"INSERT INTO admin VALUES ('{self.username}', '{self.__password}')"
        self.execute_query(query) 

    def ambil_data(self):
        query = f"select * from admin where username='{self.username}'"
        data = self.execute_query(query).fetchall()
        return data

    def cek_user(self):
        data = self.ambil_data()
        if self.username == data[0][0]:
            if self.__password == data[0][1]:
                return "200"
        else:
            return "404"
        
        # fungsinya sama tetapi perilakunya berbeda#
        #kenapa dia inherintance karena dia mengamnbil dari satu sifat dari kelas induk yaitu def init
