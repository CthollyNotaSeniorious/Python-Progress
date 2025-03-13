#Struktur dasar function

def nama_fungsi(parameter1, parameter2):
  hasil = parameter1 + parameter2
  return hasil

#Contoh
def sapa(): #Declare function
  print("Halooo")

sapa() #Manggil fungsi

#Yang pake parameter
def sapa(nama):
  print(f"Haloo {nama}, Selamat Pagi!")

sapa("Ferdii") # Manggil fungsi pake argumen

#Yang pake return value

def tambah(a, b):
  return a + b

hasil = tambah(5, 4)
print(hasil)

#Default parameter function
def sapa(nama = "Ferdii"):
  print(f"Selamat pagi {nama}!")

sapa()
sapa("Hu Tao")

#Multiple parameters function
def jumlahkan(*angka):
    return sum(angka)

print(jumlahkan(1, 2, 3, 4, 5))  # Bisa memasukkan banyak angka

#Arguments keyword function
def data_diri(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

data_diri(nama="Ferdi", umur=21, hobi="Coding")
