"""Materi 1 - Variabel dan Tipe Data | Studi kasus: Klinik Hewan PawCare.

Tujuan : menyimpan data satu pasien (hewan) dalam variabel dengan tipe yang sesuai.
Data   : nama, jenis, umur, berat, status vaksin.
Proses : isi variabel -> tampilkan data -> cek tipe tiap variabel.
"""
nama_hewan = "Mochi"      # str
jenis = "Kucing"          # str
umur = 3                  # int
berat = 4.5               # float
sudah_vaksin = True       # bool

print(f"{nama_hewan} ({jenis}), umur {umur} tahun, berat {berat} kg")
print(f"Sudah vaksin: {sudah_vaksin}")
print(type(nama_hewan), type(jenis), type(umur), type(berat), type(sudah_vaksin))

# Data pengganti untuk demo: "Bruno", "Anjing", 7, 12.8, False
