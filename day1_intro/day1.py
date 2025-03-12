# Aku belajar komentar python
# ini komentar

"""
ini komentar
multiline
"""

nama = "Ferdi"            #tipe data string
kelas = "Informatika A"   #tipe data string
usia = 18                 #tipe data integer
tinggi = 160.5            #tipe data float
is_student = True         #tipe data boolean

print("hallo perkenalkan nama saya", nama)
print("hallo perkenalkan nama saya {nama}")
print(f"hallo perkenalkan nama saya {nama}") #penggunaan f-string dibutuhkan agar ekspresi kurung kurawal dapat dipakai
print("saya berusia", usia, "dan tinggi saya", tinggi)
print("apakah saya adalah mahasiswa?", is_student)

# ini tipe data dasar

bilangan_bulat = 10       #tipe data integer
bilangan_desimal = 2.5    #tipe data float
teks = "aku suka coding"  #tipe data string
benar_salah = True        #tipe data boolean
tida_ada = None           #tipe data none/tidak memiliki nilai

# operator aritmatika

print(5 + 3)    #penjumlahan
print(10 - 4)   #pengurangan
print(6 * 7)    #perkalian
print(8 / 2)    #pembagian
print(9 // 2)   #pembagian dengan pembulatan ke bawah
print(10 % 3)   #sisa pembagian
print(2 ** 3)   #pangkat

#operator logika
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

#pengkondisian

x = 10

if (x > 5):
  print ("x lebih besar dari 5")
elif (x < 5):
  print ("x lebih kecil dari 5")
else:
  print ("x sama dengan 5")