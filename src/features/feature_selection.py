# Feature Engineering

#Mengambil Hanya yang berkorelasi tinggi dengan target
fitur_pilihan = ["rasio_pinjaman_terhadap_pendapatan", "gagal_bayar_tercatat", "tunggakan_2thn_terakhir", "skor_kredit", "usia", "lama_riwayat_kredit_tahun"]

X = df[fitur_pilihan]
y = df["status_pinjaman"]

print(X.head())
print(y.head())


