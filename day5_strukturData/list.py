# List kosong
daftar_kosong = []

# List dengan beberapa elemen
angka = [1, 2, 3, 4, 5]
nama = ["Andi", "Budi", "Citra"]
campuran = [10, "Python", 3.14, True]

print(nama[0])  # Output: Andi  (indeks dimulai dari 0)
print(nama[-1]) # Output: Citra (mengakses dari belakang)

nama[1] = "Dewi"  # Mengubah elemen kedua
print(nama)  # Output: ['Andi', 'Dewi', 'Citra']

angka.append(6)      # Menambahkan di akhir
angka.insert(2, 10)  # Menyisipkan di indeks 2
angka.remove(3)      # Menghapus angka 3
print(angka)

for item in nama:
    print(item)