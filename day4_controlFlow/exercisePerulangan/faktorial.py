# Buat program yang menghitung faktorial dari sebuah bilangan N menggunakan perulangan for atau while.

# 📌 Faktorial:

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 3! = 3 × 2 × 1 = 6
# 📌 Contoh Input & Output:

# Masukkan N: 5
# Output: Faktorial dari 5 adalah 120

N = int(input("Masukkan angka: "))
faktorial = 1

for i in range(1, N + 1):
    faktorial *= i

print(f"Faktorial dari {N} adalah {faktorial}")