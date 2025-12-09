import pandas as pd


data = {
    'Tanggal': ['2025-11-01', '2025-11-01', '2025-11-02', '2025-11-02', '2025-11-03', '2025-11-03'],
    'Cabang': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Produk': ['Sabun', 'Sampo', 'Pasta Gigi', 'Sabun', 'Sampo', 'Pasta Gigi'],
    'Penjualan': [50000, 75000, 40000, 60000, 90000, 30000]
}

df = pd.DataFrame(data)

# Operasi agregasi: total dan rata-rata penjualan per cabang
hasil_agregasi = df.groupby('Cabang').agg({
    'Penjualan': ['sum', 'mean', 'max', 'min', 'count']
})


hasil_agregasi.columns = ['Total Penjualan', 'Rata-rata Penjualan', 'Penjualan Tertinggi', 'Penjualan Terendah', 'Jumlah Transaksi']
print(hasil_agregasi)