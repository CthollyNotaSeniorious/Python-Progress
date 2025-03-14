# #Tugas 4: Fungsi dengan Looping

# Buatlah fungsi yang menerima sebuah angka sebagai input dan
# mengembalikan hasil penjumlahan dari 1 hingga angka tersebut.

def angka(bil1):
  total = 0
  for i in range(1, bil1 + 1):
    total += i

  return total

hasil = angka(int(input("Masukkan angka: ")))

print(hasil)