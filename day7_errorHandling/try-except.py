try:
    angka = int(input("Masukkan angka: "))  # Bisa error jika input bukan angka
    hasil = 10 / angka  # Bisa error jika angka = 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Masukkan harus berupa angka!")
except Exception as e:
    print("Terjadi error:", e)