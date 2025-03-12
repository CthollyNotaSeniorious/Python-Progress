angka = int(input("Masukkan angka: "))
faktorial = 1

for i in range(1, angka + 1):
  faktorial *= i
  #1 faktorial = faktorial * 1 = 1
  #2 faktorial = faktorial * 2 = 2
  #3 faktorial = faktorial * 3 = 6
  #4 faktorial = faktorial * 4 = 24
  #5 faktorial = faktorial * 5 = 120

print(f"Jadi faktorial dari {angka} adalah {faktorial}")