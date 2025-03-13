# Buat dictionary dengan struktur berikut:

# mahasiswa = {
#     "nama": "Budi",
#     "usia": 20,
#     "jurusan": "Informatika"
# }
# Lalu:

# Tambahkan key "universitas" dengan nilai "Universitas Sam Ratulangi".
# Ubah usia menjadi 21.
# Hapus key "jurusan".
# Cetak dictionary hasil akhirnya.

mahasiswa = {
    "nama": "Budi",
    "usia": 20,
    "jurusan": "Informatika"
}

mahasiswa["universitas"] = "Universitas Sam Ratulangi"
mahasiswa["usia"] = 21
del mahasiswa["jurusan"]

print(mahasiswa)