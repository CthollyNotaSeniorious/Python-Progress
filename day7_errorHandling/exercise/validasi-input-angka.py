# 1️⃣ Soal: Validasi Input Angka
# Buat program yang meminta user memasukkan angka bulat. Jika user memasukkan teks atau karakter lain, tampilkan pesan error:
# 📌 "Input harus berupa angka!"
# 🔹 Gunakan try-except untuk menangani ValueError.

try:
  angka = int(input("Masukkan angka bulat: "))
  print("Input berhasil!")
except ValueError:
  print("Error angka harus bulat!")