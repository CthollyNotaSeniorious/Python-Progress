print("Selamat datang, apa yang Anda ingin beli hari ini?")
print("1. Minyak 1L = RP17.000")
print("2. Gula Pasir 1KG = RP15.000")
print("3. Crackers = RP1.000")
print("4. Beras 1KG = RP16.000")

minyak = 17000
gulaPasir = 15000
crackers = 1000
beras = 16000

total = 0

while True:
    barang = int(input("Masukkan nomor barang (0 untuk selesai): "))
    if barang == 0:
        break
    jumlah = int(input("Masukkan jumlah barang: "))

    if barang == 1:
        total += minyak * jumlah
    elif barang == 2:
        total += gulaPasir * jumlah
    elif barang == 3:
        total += crackers * jumlah
    elif barang == 4:
        total += beras * jumlah

print(f"Total harga yang harus dibayar: RP{total}")
