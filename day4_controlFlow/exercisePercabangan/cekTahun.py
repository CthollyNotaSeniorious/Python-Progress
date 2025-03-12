# Buat program untuk mengecek apakah sebuah tahun adalah tahun kabisat atau tidak.
# 📌 Tahun kabisat adalah:

# Habis dibagi 400 atau
# Habis dibagi 4 tetapi tidak habis dibagi 100
# 📌 Contoh Input & Output:

# Masukkan tahun: 2024
# Output: 2024 adalah tahun kabisat

tahun = int(input("Masukkan Tahun: "))

if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print(f"{tahun} Tahun kabisat")
else:
    print(f"{tahun} Bukan tahun kabisat")