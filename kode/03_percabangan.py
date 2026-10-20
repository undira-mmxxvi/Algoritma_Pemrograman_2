"""Materi 3 - Percabangan | Studi kasus: Klinik Hewan PawCare.

Tujuan : menentukan kategori ukuran hewan dan dosis obat cacing.
Data   : berat hewan (kg).
Proses : if / elif / else memilih satu dari tiga cabang.
"""
berat = 4.5

if berat < 3:
    kategori, dosis = "Kecil", 0.5
elif berat <= 10:
    kategori, dosis = "Sedang", 1.0
else:
    kategori, dosis = "Besar", 2.0

print(f"Berat {berat} kg -> kategori: {kategori}, dosis obat cacing: {dosis} tablet")

# Percabangan bersarang: status vaksin
sudah_vaksin = False
if sudah_vaksin:
    print("Vaksin lengkap, tidak perlu vaksin ulang.")
else:
    if berat >= 2:
        print("Boleh divaksin hari ini.")
    else:
        print("Berat terlalu kecil, tunda vaksin.")

# Data pengganti: berat = 2.0, lalu berat = 15 (ketiga cabang tampil)
