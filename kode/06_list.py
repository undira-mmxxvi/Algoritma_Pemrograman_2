"""Materi 6 - List | Studi kasus: Klinik Hewan PawCare.

Tujuan : mengelola antrean pasien yang bisa berubah.
Data   : daftar nama pasien dan daftar berat pasien.
Proses : append, remove, insert, pop, sort, indexing, slicing, list comprehension.
"""
antrean = ["Mochi", "Bruno", "Luna"]
antrean.append("Kiki")           # pasien baru datang
antrean.remove("Bruno")          # pasien batal
antrean.insert(0, "Darurat")     # kasus darurat didahulukan
dipanggil = antrean.pop(0)       # panggil pasien pertama
print("Dipanggil:", dipanggil)

antrean.sort()
print("Antrean:", antrean)
print("Jumlah:", len(antrean))
print("Pertama:", antrean[0], "| Terakhir:", antrean[-1])
print("Dua teratas:", antrean[:2])

berat_pasien = [4.5, 12.8, 3.2, 6.0]
print("Rata-rata berat:", round(sum(berat_pasien) / len(berat_pasien), 2))
print("Berat > 5 kg:", [b for b in berat_pasien if b > 5])

# Data pengganti: tambah dan hapus nama pasien lain, ubah isi berat_pasien
