"""Materi 5 - Dictionary | Studi kasus: Klinik Hewan PawCare.

Tujuan : menyimpan data pasien berpasangan key-value dan daftar harga layanan.
Data   : profil pasien, harga layanan.
Proses : akses, ubah, tambah, hapus key; iterasi items(); dictionary bersarang.
"""
pasien = {
    "nama": "Mochi",
    "jenis": "Kucing",
    "umur": 3,
    "berat": 4.5,
    "sudah_vaksin": False,
}

print("Nama:", pasien["nama"])
pasien["sudah_vaksin"] = True          # ubah nilai
pasien["pemilik"] = "Budi"             # tambah key baru
del pasien["umur"]                     # hapus key
print("Umur ada?", "umur" in pasien)
print("Alergi:", pasien.get("alergi", "tidak ada data"))

for kunci, nilai in pasien.items():
    print(f"  {kunci}: {nilai}")

harga = {"Pemeriksaan": 75000, "Vaksinasi": 120000, "Grooming": 90000}
harga["Vaksinasi"] = 130000            # tarif naik
print("Layanan termahal:", max(harga, key=harga.get))
print("Total semua layanan:", sum(harga.values()))

# Dictionary bersarang: banyak pasien
data_pasien = {
    "P001": {"nama": "Mochi", "jenis": "Kucing"},
    "P002": {"nama": "Bruno", "jenis": "Anjing"},
}
for kode, info in data_pasien.items():
    print(kode, "->", info["nama"], f"({info['jenis']})")

# Data pengganti: ubah harga Vaksinasi, tambah pasien P003
