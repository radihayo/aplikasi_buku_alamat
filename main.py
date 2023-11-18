from flask import Flask, jsonify, request
import crud_function
from db import create_table

# list route
# read_data, menampilkan seluruh data dari tabel
# insert_data, menambahkan data baru
# detail_data/id, menampilkan data berdasarkan id
# search_data_nama/nama, menampilkan seluruh data berdasarkan nama
# search_data_no_telp/no_telp, menampilkan seluruh data berdasarkan nomor telepon
# search_data_alamat/alamat, menampilkan seluruh data berdasarkan alamat
# delete_data/id, menghapus data berdasarkan id

app = Flask(__name__)


@app.route("/read_data", methods=["GET"])
def get_data():
    result = crud_function.get_data()
    return jsonify(result)


@app.route("/insert_data", methods=["POST"])
def insert_data():
    kontak = request.get_json()
    nama = kontak["nama"]
    no_telp = kontak["no_telp"]
    alamat = kontak["alamat"]
    result = crud_function.insert_data(nama, no_telp, alamat)
    return jsonify(result)


@app.route("/detail_data/<id>", methods=["GET"])
def get_data_by_id(id):
    result = crud_function.get_data_by_id(id)
    return jsonify(result)


@app.route("/search_data_nama/<nama>", methods=["GET"])
def search_data_by_nama(nama):
    result = crud_function.search_data_by_nama(nama)
    return jsonify(result)


@app.route("/search_data_no_telp/<no_telp>", methods=["GET"])
def search_data_by_no_telp(no_telp):
    result = crud_function.search_data_by_no_telp(no_telp)
    return jsonify(result)


@app.route("/search_data_alamat/<alamat>", methods=["GET"])
def search_data_by_alamat(alamat):
    result = crud_function.search_data_by_alamat(alamat)
    return jsonify(result)


@app.route("/delete_data/<id>", methods=["DELETE"])
def delete_data(id):
    result = crud_function.delete_data(id)
    return jsonify(result)


if __name__ == "__main__":
    create_table()
    app.run(host='0.0.0.0', port=8000, debug=True)
