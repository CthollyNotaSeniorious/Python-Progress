# Hello World
print("Hello World")

# Menghitung luas persegi
sisi = input("Masukkan panjang sisi: ")
sisi = float(sisi)

luas = sisi * sisi

print(f"Luas persegi adalah {luas}")

# Buat program yang meminta nama dan umur pengguna, lalu mencetak kalimat seperti:
# "Halo, nama saya Ferdi dan saya berusia 20 tahun."
nama = input("Masukkan nama anda: ")
umur = input("Masukkan umur anda: ")

print(f"Halo, nama saya {nama} dan saya berusia {umur} tahun.")

# Buat program yang meminta pengguna memasukkan sebuah angka, kemudian mencetak apakah angka tersebut genap atau ganjil.
# Petunjuk: Gunakan operator modulus (%)
# Jika angka % 2 == 0, maka angka tersebut genap
angka = int(input("Masukkan angka :"))

if (angka % 2 == 0) :
  print("Angka tersebut genap")
elif (angka % 2 == 1):
  print("Angka tersebut ganjil")
else: 
  print("Error")