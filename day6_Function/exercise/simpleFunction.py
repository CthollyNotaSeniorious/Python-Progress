# Tugas 1: Fungsi Sederhana
# Buatlah fungsi yang menerima dua buah angka sebagai input dan mengembalikan hasil penjumlahan kedua angka tersebut.

def angka(angka1, angka2):
  return angka1 + angka2

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = angka(angka1, angka2)
print(hasil)