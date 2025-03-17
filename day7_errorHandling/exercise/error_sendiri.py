# 5️⃣ Soal: Buat Error Sendiri dengan Raise
# Buat fungsi cek_usia() yang meminta user memasukkan usia.
# Jika usia kurang dari 18, tampilkan error menggunakan raise ValueError:
# 📌 "Usia harus minimal 18 tahun!"

def cek_usia():
    usia = int(input("Masukkan usia anda: "))
    if usia < 18:
        raise ValueError("Usia harus minimal 18 tahun!")

try:
    cek_usia()
    print("Akses diizinkan!")
except ValueError as e:
    print(f"Error: {e}")
