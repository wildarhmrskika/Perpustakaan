import sqlite3

# Putri Angraini Aziz E1E122074
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

# Rosalina E1E122138
class Buku(DatabaseManager): #ini inheritance
    def __init__(self, db_file, judul, kategori, deskripsi, file, sampul):
        super().__init__(db_file)
        self.judul = judul
        self.kategori = kategori
        self.deskripsi = deskripsi
        self.file = file
        self.sampul = sampul

    def tambah_data(self):
        query = f"INSERT INTO terbaru VALUES (null, '{self.judul}', '{self.kategori}', '{self.deskripsi}', '{self.file}', '{self.sampul}')"
        self.execute_query(query)


# Wilda Rahma Riskika E1E122035
class KelolaBuku(DatabaseManager): #ini inheritance
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


# Rahma Damayanti E1E122076
class User(DatabaseManager):#ini inheritance
    def __init__(self, db_file, username, password):
        super().__init__(db_file)
        self.username = username
        self.__password = password 

    def tambah_data(self):
        query = f"INSERT INTO admin VALUES ('{self.__username}', '{self.__password}')" #ini termaksud enkapsulasi karna pada fungsi tambahkan data terdapat self.__username dibuat menjadi privat yang dimana hanya bisa di akses oleh kelas user
        self.execute_query(query) 

    def ambil_data(self):
        query = f"select * from admin where username='{self.__username}'"
        data = self.execute_query(query).fetchall()
        return data

    def cek_user(self):
        data = self.ambil_data()
        if self.__username == data[0][0]:
            if self.__password == data[0][1]:
                return "200"
        else:
            return "404"
        

#update