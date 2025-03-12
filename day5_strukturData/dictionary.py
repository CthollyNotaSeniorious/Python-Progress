mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa["nama"])   # Output: Andi
print(mahasiswa.get("umur"))  # Output: 20

mahasiswa["semester"] = 4  # Menambahkan data baru
mahasiswa["umur"] = 21      # Mengubah umur

del mahasiswa["jurusan"]  # Menghapus elemen
for key, value in mahasiswa.items():
    print(key, ":", value)
