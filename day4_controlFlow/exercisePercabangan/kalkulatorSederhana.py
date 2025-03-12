# Buat program yang meminta dua angka dan *operator (+, -, , /) dari pengguna, lalu tampilkan hasil perhitungannya.

# 📌 Contoh Input & Output:

# Masukkan angka pertama: 10  
# Masukkan operator (+, -, *, /): *  
# Masukkan angka kedua: 5  
# Output: 10 * 5 = 50

bil1 = float(input("Masukkan angka pertama: "))
print("Operator:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
op = int(input("Masukkan operator: "))
bil2 = float(input("Masukkan angka kedua: "))

if(op == 1):
  print(f"{bil1} + {bil2} = ", (bil1 + bil2))
elif(op == 2):
  print(f"{bil1} - {bil2} = ", (bil1 - bil2))
elif(op == 3):
  print(f"{bil1} * {bil2} = ", (bil1 * bil2))
elif(op == 4):
  print(f"{bil1} / {bil2} = ", (bil1 / bil2))
else:
  print("Error")