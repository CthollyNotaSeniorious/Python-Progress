# Buat program yang meminta pengguna memasukkan sebuah angka N, lalu cetak semua bilangan ganjil dari 1 hingga N.

# 📌 Contoh Input & Output:

# Masukkan N: 10
# Output: 1 3 5 7 9

i = 1

n = int(input("Masukkan N: "))

while i < n + 1:
    print(i)
    i += 2