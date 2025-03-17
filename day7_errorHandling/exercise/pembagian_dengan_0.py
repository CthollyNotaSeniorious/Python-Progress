# 2️⃣ Soal: Pembagian dengan Nol
# Buat program yang meminta user memasukkan dua angka, lalu lakukan pembagian.
# 📌 Jika user memasukkan nol sebagai pembagi, tangkap ZeroDivisionError dan tampilkan pesan:
# ✅ "Error: Tidak bisa membagi dengan nol!"

while True:
  try:
      angka1 = float(input("Masukkan angka pertama: "))
      angka2 = float(input("Masukkan angka kedua: "))
      hasil = angka1 / angka2
      print(f"Hasil dari operasi yaitu {hasil}")
      break
  except ZeroDivisionError:
      print("Error: Tidak dapat membagi dengan 0! Silakan masukkan angka lain.")
  except ValueError:
      print("Error: Input harus berupa angka! Coba lagi.")
  except Exception as e:
      print(f"Terjadi error tak terduga: {e}")
