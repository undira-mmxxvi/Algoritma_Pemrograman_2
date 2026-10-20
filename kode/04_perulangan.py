"""Materi 4 - Perulangan | Studi kasus: Klinik Hewan PawCare.

Tujuan : menampilkan daftar layanan, memanggil antrean, dan menghitung total tarif.
Data   : daftar layanan, jumlah antrean, daftar tarif.
Proses : for + enumerate, while dengan penghitung, break/continue.
"""
layanan = ["Pemeriksaan", "Vaksinasi", "Grooming"]
tarif = [75000, 120000, 90000]

# for: daftar layanan bernomor + total tarif
total = 0
for i, nama in enumerate(layanan, start=1):
    print(f"{i}. {nama} - Rp{tarif[i - 1]:,}")
    total += tarif[i - 1]
print("Total semua layanan:", f"Rp{total:,}")

# while: memanggil antrean sampai habis
sisa_antrean = 3
while sisa_antrean > 0:
    print(f"Memanggil pasien... sisa antrean: {sisa_antrean}")
    sisa_antrean -= 1
print("Antrean kosong.")

# continue / break: lewati layanan Grooming, berhenti di layanan mahal
for nama, harga in zip(layanan, tarif):
    if nama == "Grooming":
        continue
    print("Diproses:", nama)
    if harga > 100000:
        print("Layanan mahal, hentikan proses.")
        break

# Data pengganti: tambah satu layanan (dan tarifnya), sisa_antrean = 5
