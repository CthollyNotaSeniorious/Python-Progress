# 5️⃣ List & Looping:
# Buat program yang meminta input sejumlah nama mahasiswa, lalu simpan dalam list. Cetak nama-nama tersebut dalam urutan terbalik.

namaMahasiswa = []
while True:
  nama = str(input("Masukkan nama mahasiswa, ketik 0 untuk mengakhiri: "))
  if nama == "0" :
    break
  namaMahasiswa.append(nama)

namaMahasiswa.sort(reverse=True)

print(namaMahasiswa)