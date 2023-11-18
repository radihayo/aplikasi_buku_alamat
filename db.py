import sqlite3


def connect_db():
    connect = sqlite3.connect('db_kontak.db')
    return connect


def create_table():
    try:
        tables = [
            """CREATE TABLE IF NOT EXISTS tbl_kontak(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
				no_telp TEXT NOT NULL,
				alamat TEXT NOT NULL
            )
            """
        ]
        db = connect_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)
        print('Tabel berhasil dibuat')
    except:
        print('Tabel gagal dibuat')
