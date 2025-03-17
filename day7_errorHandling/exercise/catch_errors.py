# 3️⃣ Soal: Menangkap Semua Error
# Buat program yang meminta user memasukkan dua angka,
# lalu lakukan operasi penjumlahan, pengurangan, perkalian,
# atau pembagian sesuai pilihan user.
# 📌 Jika terjadi kesalahan (seperti input salah
# atau pembagian dengan nol), tangkap dengan Exception
# dan tampilkan pesan error yang sesuai.

while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        operator = input("Masukkan operator (Tambah, Kurang, Kali, Bagi): ")

        match operator:
            case "Tambah":
                print(f"Hasil penjumlahannya yaitu {angka1 + angka2}")
            case "Kurang":
                print(f"Hasil pengurangannya yaitu {angka1 - angka2}")
            case "Kali":
                print(f"Hasil perkaliannya yaitu {angka1 * angka2}")
            case "Bagi":
                print(f"Hasil pembagiannya yaitu {angka1 / angka2}")
            case _:
                print("Error: Operator tidak valid! Silakan coba lagi.")
                continue

        break

    except ZeroDivisionError:
        print("Error: Tidak dapat membagi dengan 0! Silakan masukkan angka lain.")
    except ValueError:
        print("Error: Input harus berupa angka! Coba lagi.")
    except Exception as e:
        print(f"Terjadi error tak terduga: {e}")
