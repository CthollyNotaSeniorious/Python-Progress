# Buat program untuk mencetak pola segitiga bintang dengan tinggi N.

# 📌 Contoh Input & Output:

# Masukkan tinggi segitiga: 5
# Output:
# *
# **
# ***
# ****
# *****

x = int(input("Masukkan tinggi segitiga: "))

for i in range(1, x + 1):
  print(i * "*")