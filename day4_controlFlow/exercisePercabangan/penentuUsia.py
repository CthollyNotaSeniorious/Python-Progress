# Buat program yang meminta umur seseorang, lalu tampilkan kategorinya:

# 0 - 5 tahun → "Balita"
# 6 - 12 tahun → "Anak-anak"
# 13 - 17 tahun → "Remaja"
# 18 tahun ke atas → "Dewasa"
while True:
  usia = int(input("Masukkan usia: "))

  if(0 <= usia <= 5):
    print("Balita")
  elif(6 <= usia <= 12):
    print("Anak-anak")
  elif(13 <= usia <= 17):
    print("Remaja")
  elif(18 <= usia):
    print("Dewasa")