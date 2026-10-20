"""Materi 7 - Tuple | Studi kasus: Klinik Hewan PawCare.

Tujuan : menyimpan data tetap klinik yang tidak boleh berubah.
Data   : jam operasional, koordinat klinik, hari libur.
Proses : unpacking, indexing, count, error saat tuple diubah, konversi ke list.
"""
jam_operasional = ("08:00", "17:00")
koordinat_klinik = (-6.2088, 106.8456)
hari_libur = ("Minggu", "Minggu", "Senin")

buka, tutup = jam_operasional     # unpacking
lat, lon = koordinat_klinik
print(f"Buka {buka} - {tutup}")
print(f"Lokasi: lat {lat}, lon {lon}")
print("Jam tutup:", jam_operasional[1])
print("Berapa kali 'Minggu':", hari_libur.count("Minggu"))

try:
    jam_operasional[0] = "09:00"
except TypeError as e:
    print("Tuple tidak bisa diubah ->", e)

# Cara mengubah: konversi ke list, lalu kembali ke tuple
sementara = list(jam_operasional)
sementara[0] = "09:00"
jam_operasional = tuple(sementara)
print("Jam baru:", jam_operasional)

# Data pengganti: ubah jam operasional menjadi ("07:30", "20:00")
