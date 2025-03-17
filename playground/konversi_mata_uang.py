print("Selamat datang, mata uang apa yang ingin anda konversi?")
print("1. IDR")
print("2. USD")
print("3. JPY")

mataUangAwal = int(input("Masukkan nomor mata uang awal anda: "))
nominal = int(input("Masukkan nominal uang yang ingin anda konversi: "))
mataUangAkhir = int(input("Masukkan nomor mata uang yang anda inginkan: "))

mataUang = {
  1: "RP",
  2: "USD",
  3: "JPY"
}



def hasilKonversi(mataUangAwal, nominal, mataUangAkhir):
  if mataUangAwal == 1 and mataUangAkhir == 2:
    return nominal / 15000
  if mataUangAwal == 1 and mataUangAkhir == 3:
    return nominal / 100
  if mataUangAwal == 2 and mataUangAkhir == 1:
    return nominal * 15000
  if mataUangAwal == 2 and mataUangAkhir == 3:
    return nominal * 150
  if mataUangAwal == 3 and mataUangAkhir == 1:
    return nominal * 100
  if mataUangAwal == 3 and mataUangAkhir == 2:
    return nominal / 150
  
print("Hasil akhir nominal anda adalah", hasilKonversi(mataUangAwal, nominal, mataUangAkhir), mataUang[mataUangAkhir])