print ("Kalkulator Sederhana")
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
operasi = int(input("Masukkan jenis operasi: "))

if(operasi == 1):
  print(f"Hasil penjumlahan bilangan 1 dan bilangan 2 adalah{num1 + num2}")
elif(operasi == 2):
  print(f"Hasil pengurangan bilangan 1 dan bilangan 2 adalah{num1 - num2}")
elif(operasi == 3):
  print(f"Hasil perkalian bilangan 1 dan bilangan 2 adalah{num1 * num2}")
elif(operasi == 4):
  print(f"Hasil perkalian bilangan 1 dan bilangan 2 adalah{num1 / num2}")
else:
  print("error")