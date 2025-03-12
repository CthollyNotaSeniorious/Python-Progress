# Buat program yang meminta pengguna memasukkan 5 nama teman,
# lalu simpan dalam list dan tampilkan semua nama tersebut satu per satu.

Nama = []
for i in range (1, 6):
  nama = str(input(f"Masukkan nama teman ke-{i}: "))
  Nama.append(nama)

print("Daftar temanmu:")
for n in range (0, 5):
  print("- ", Nama[n])