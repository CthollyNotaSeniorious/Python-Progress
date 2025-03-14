# Tugas 7: Fungsi dengan Dictionary

# Buatlah fungsi yang menerima sebuah dictionary sebagai input dan
# mengembalikan hasil penjumlahan dari semua nilai dalam dictionary tersebut.

def dictionary(dict):
  total = 0
  for value in dict.values():
    total += value
  return total

dict = {}

for i in range(1, 5):
  Angka = int(input("Masukkan angka: "))
  dict[f"Angka{i}"] = Angka

print(dictionary(dict))