from db import connect_db
import re


def insert_data(nama, no_telp, alamat):
    db = connect_db()
    cursor = db.cursor()
    if nama == "" or no_telp == "" or alamat == "":
        message = "Salah satu inputan kosong"
    elif not re.match("[A-Za-z]", nama):
        message = "Nama harus alphabet"
    elif not re.match("[0-9]", no_telp):
        message = "Nomor telepon harus angka"
    else:
        statement = "INSERT INTO tbl_kontak(nama, no_telp, alamat) VALUES (?, ?, ?)"
        cursor.execute(statement, [nama, no_telp, alamat])
        db.commit()
        message = "Data dengan nama " + nama + " berhasil ditambahkan"
    return message


def get_data():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT id, nama, no_telp, alamat FROM tbl_kontak"
    cursor.execute(query)
    get_data = cursor.fetchall()
    if len(get_data) == 0:
        get_data = "Tidak ada data"
    else:
        get_data = get_data
    return get_data


def get_data_by_id(id):
    db = connect_db()
    cursor = db.cursor()
    statement = "SELECT id, nama, no_telp, alamat FROM tbl_kontak WHERE id = ?"
    cursor.execute(statement, [id])
    get_data = cursor.fetchone()
    if get_data:
        get_data = get_data
    else:
        get_data = "Tidak ada data"
    return get_data


def search_data_by_nama(nama):
    db = connect_db()
    cursor = db.cursor()
    statement = "SELECT id, nama, no_telp, alamat FROM tbl_kontak WHERE nama = ?"
    cursor.execute(statement, [nama])
    get_data = cursor.fetchall()
    if get_data:
        get_data = get_data
    else:
        get_data = "Tidak ada data"
    return get_data


def search_data_by_no_telp(no_telp):
    db = connect_db()
    cursor = db.cursor()
    statement = "SELECT id, nama, no_telp, alamat FROM tbl_kontak WHERE no_telp = ?"
    cursor.execute(statement, [no_telp])
    get_data = cursor.fetchall()
    if get_data:
        get_data = get_data
    else:
        get_data = "Tidak ada data"
    return get_data


def search_data_by_alamat(alamat):
    db = connect_db()
    cursor = db.cursor()
    statement = "SELECT id, nama, no_telp, alamat FROM tbl_kontak WHERE alamat = ?"
    cursor.execute(statement, [alamat])
    get_data = cursor.fetchall()
    if get_data:
        get_data = get_data
    else:
        get_data = "Tidak ada data"
    return get_data


def delete_data(id):
    db = connect_db()
    cursor = db.cursor()
    statement = "DELETE FROM tbl_kontak WHERE id = ?"
    cursor.execute(statement, [id])
    run_query = db.commit()
    if run_query:
        run_query = run_query
    else:
        run_query = "Tidak ada data"
    return run_query
