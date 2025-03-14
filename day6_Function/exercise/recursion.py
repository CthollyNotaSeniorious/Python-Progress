# Tugas 8: Fungsi dengan Recursion

# Buatlah fungsi yang menerima sebuah angka sebagai input dan mengembalikan hasil
# faktorial dari angka tersebut menggunakan teknik rekursi.

def faktorial(n):
  if n == 0:
    return 1
  else:
    return n * faktorial(n - 1)

n = int(input("Masukkan Angka: "))

print(f"Hasil faktorial dari {n} adalah {faktorial(n)}")