# Tugas 3: Fungsi dengan Return Value

# Buatlah fungsi yang menerima sebuah angka sebagai input dan
# mengembalikan nilai kuadrat dari angka tersebut.

def angka(bil):
  bil = bil**2
  return bil

hasil = angka(int(input("Masukkan angka: ")))
print(hasil)