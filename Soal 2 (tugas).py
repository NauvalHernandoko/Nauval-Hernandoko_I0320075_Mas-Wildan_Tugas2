#tipe data string
tipe_data = "tipe data string"
print("bertipe:" ,tipe_data)
nama_lengkap = "Nauval Hernandoko"
print("nama lengkap:" ,nama_lengkap)
jenis_kelamin = "Laki-laki"
print("jenis kelamin:" ,jenis_kelamin)
alamat = """
    Tunjungsari, Mlese, Gantiwarno, Klaten
    """""
print("alamat:" ,alamat)
agama = "Islam"
print("agama: " ,agama)
riwayat_pendidikan = """
        SD N Gesikan, SMP N 1 Wedi, SMA N 1 Klaten, Teknik Industri UNS
        """""
print("riwayat pendidikan:" ,riwayat_pendidikan)
hobi = "Bermain musik dan futsal"
print("hobi:" ,hobi)
nama_orang_tua = "Sadhaka Budiyanto"
print("nama orang tua:" ,nama_orang_tua)
pekerjaan_orang_tua = "Guru"
print("pekerjaan orang tua:" ,pekerjaan_orang_tua)

print("========================================================")

#tipe data integer
tipe_data2 = "tipe data integer"
print("bertipe:" ,tipe_data2)

umur_sekarang = 18
print("umur:" ,umur_sekarang)
umur_bulan = umur_sekarang * 12 + 11                               #menghitung umur dalam bulan
print("umur dalam bulan:" ,umur_bulan)
umur_hari1 = umur_bulan * 30                                       #asumsi 1 bulan 30 hari
print("umur dalam hari1:" ,umur_hari1)
umur_hari2 = umur_bulan * 31                                       #asumsi 1 bulan 31 hari
print("umur dalam hari2:" ,umur_hari2)
print("umur dalam hari1 < umur dalam hari < umur dalam hari2")
umur_hari = 18 * 365 + (365-31)                                    #asumsi 1 tahun 365 hari
print("umur hari (perhitungan tahun):" ,umur_hari)

tinggi_badan = 174
print("tinggi badan:" ,tinggi_badan)
ukuran_sepatu = 41
print("ukuran sepatu:" ,ukuran_sepatu)
berat_badan = 56
print("berat badan:" ,berat_badan)

print("=======================================================")

print("rumus menghitung volume tabung")
T = int(input("masukkan nilai tinggi tabung: "))
r = int(input("masukkan nilai jari-jari: "))
V_tab = 3.14 * r * r * T
print("volume tabung: " ,V_tab)

print("=======================================================")

#tipe data float
tipe_data3 = "tipe data float"
print("bertipe:" ,tipe_data3)

print("rumus menghitung berat badan ideal")
tinggi_badan = float(input("masukkan tinggi badan: "))
print("tinggi_badan")
berat_badan_ideal = (float(tinggi_badan) - 100) - ((float(tinggi_badan) - 100) * 10 / 100)
print("BBI:" ,berat_badan_ideal)

print("=======================================================")

print("rumus menghitung daya")
W = float(input("masukkan nilai usaha: "))
delta_t = float(input("masukkan nilai perubahan waktu: "))
P = W / delta_t
print("P: " ,P)

print("=======================================================")

#terdapat 2 pilihan rumus
print("apakah yang akan dihitung?")
print("1. Gerak lurus beraturan")
print("2. Gerak lurus berubah beraturan")

choice = input("masukkan pilihan: ")

if choice == "1" :
    print("rumus menghitung kecepatan GLB")
    s = float(input("masukkan jarak dalam meter: "))
    ts = float(input("masukkan waktu dalam sekon: "))
    v = s / ts
print("v: " ,v)

if choice == "2" :
    print("rumus menghitung GLBB")
    v0 = float(input("masukkan nilai kecepatan awal: "))
    a = float(input("masukan nilai percepatan: "))
    t = float(input("masukkan nilai waktu: "))
    vt = v0 + a * t
    print("vt: " ,vt)









