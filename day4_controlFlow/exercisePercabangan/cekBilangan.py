# Masukkan angka: -5
# Output: Bilangan negatif
while True:
  angka = int(input("Masukkan angka: "))

  if(angka == 0):
    print(f"Angka {angka} adalah angka 0")
  elif(angka > 0):
    print(f"Angla {angka} adalah angka positif")
  elif(angka < 0):
    print(f"Angka {angka} adalah angka negatif")
  else :
    print("Error")
