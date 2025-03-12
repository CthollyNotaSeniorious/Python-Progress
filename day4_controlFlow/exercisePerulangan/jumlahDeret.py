# Buat program yang menjumlahkan deret angka dari 1 sampai N menggunakan perulangan.

# 📌 Contoh Input & Output:

# Masukkan N: 5
# Output: 1 + 2 + 3 + 4 + 5 = 15

N = int(input("Masukkan angka: "))
faktorial = 0

for i in range(1, N + 1):
    faktorial += i

print(f"Faktorial dari {N} adalah {faktorial}")