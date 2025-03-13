# Tugas 5: Fungsi dengan Conditional Statement

# Buatlah fungsi yang menerima sebuah angka sebagai input dan mengembalikan
# kalimat yang menyebutkan apakah angka tersebut genap atau ganjil.

def angka(bil):
  if bil % 2 == 0:
    print("Bilangan tersebut adalah genap")
  elif bil % 2 == 1:
    print("Bilangan tersebut adalah ganjil")

angka(int(input("Masukkan bilangan: ")))