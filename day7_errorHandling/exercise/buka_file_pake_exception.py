# 4️⃣ Soal: Buka File dengan Exception
# Buat program yang mencoba membuka file data.txt untuk dibaca.
# 📌 Jika file tidak ditemukan, tangkap FileNotFoundError dan tampilkan pesan:
# ✅ "File tidak ditemukan! Pastikan nama file benar."

try:
    with open("data.txt", "r") as file:
        isi = file.read()
        print("Isi file:\n", isi)
except FileNotFoundError:
    print("Error! File tidak ditemukan")
