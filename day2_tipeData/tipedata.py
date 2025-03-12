nama = "Ferdi"                                      #tipe data string
umur = 18                                           #tipe data integer
tinggi = 160.5                                      #tipe data float
is_student = True                                   #tipe data boolean
data = None                                         #tipe data none
angka = [1, 2, 3, 4, 5]                             #list
koordinat = (10, 20)                                #tuple
mahasiswa = {"nama" : "Ferdi", "umur" : 18}         #dictionary

#Convert tipe data

nilai = "75"
nilai_int = int(nilai)

#String formating

print(f"nama saya {nama}, umur saya {umur}")

#menerima input dari user

nama = input("Masukkan nama : ")
umur = int(input("Masukkan umur : "))
print(f"Nama : {nama}, Umur : {umur}")

angka = 5            # Tipe data integer
desimal = 3.14       # Tipe data float
teks = "Halo"        # Tipe data string

print(type(angka))   # Output akan menunjukkan <class 'int'>
print(type(desimal)) # Output akan menunjukkan <class 'float'>
print(type(teks))    # Output akan menunjukkan <class 'str'>
