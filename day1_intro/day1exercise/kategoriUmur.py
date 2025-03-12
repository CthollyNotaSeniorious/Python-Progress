# Buat program yang meminta pengguna memasukkan umur, kemudian menentukan kategori usia dengan aturan berikut:

# Di bawah 18 tahun: "Belum dewasa"
# 18-30 tahun: "Dewasa muda"
# Di atas 30 tahun: "Dewasa"

umur = int(input("Masukkan umur: "))

if(umur < 18):
  print("Belum dewasa")
elif(umur >= 18 and umur <= 30):
  print("Dewasa muda")
elif(umur > 30):
  print("Dewasa")