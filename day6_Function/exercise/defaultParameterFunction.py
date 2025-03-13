# Tugas 2: Fungsi dengan Parameter Default

# Buatlah fungsi yang menerima nama dan umur sebagai input,
# dan mengembalikan kalimat yang menyebutkan nama dan umur.
# Jika umur tidak diisi, maka umur default adalah 20.

def dataDiri(nama, umur = 20):
  print(f"Halo, namamu adalah {nama} dan umurmu adalah {umur}")

dataDiri("Ferdii")
dataDiri("Ferdii", 18)