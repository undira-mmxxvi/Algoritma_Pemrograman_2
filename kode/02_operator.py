"""Materi 2 - Operator | Studi kasus: Klinik Hewan PawCare.

Tujuan : menghitung biaya kunjungan dan memeriksa syarat pasien.
Data   : tarif pemeriksaan, tarif vaksin, persentase diskon, umur, berat, status vaksin.
Proses : operator aritmatika (+ - * / // % **), perbandingan, logika, keanggotaan.
"""
tarif_periksa = 75000
tarif_vaksin = 120000
persen_diskon = 10
umur, berat, sudah_vaksin = 3, 4.5, False

# Aritmatika
total = tarif_periksa + tarif_vaksin
diskon = total * persen_diskon / 100
bayar = total - diskon
print("Total:", total, "| Diskon:", diskon, "| Bayar:", bayar)
print("Cicilan 3x:", bayar // 3, "sisa", bayar % 3)

# Perbandingan + logika
print("Umur >= 1 dan berat >= 3?", umur >= 1 and berat >= 3)
print("Perlu vaksin?", not sudah_vaksin)
print("Berat ekstrem (<2 atau >30)?", berat < 2 or berat > 30)

# Keanggotaan
print("Jenis dilayani?", "Kucing" in ["Kucing", "Anjing", "Kelinci"])

# Data pengganti: ubah persen_diskon, tarif, atau berat = 2.0
