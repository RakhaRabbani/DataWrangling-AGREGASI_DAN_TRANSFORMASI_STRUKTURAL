import pandas as pd

# Data berisi nilai penjualan ganda per cabang dan bulan
data = {
    'Cabang': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Bulan': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Penjualan': [100, 150, 200, 250, 300, 350]
}

df = pd.DataFrame(data)
print("=== Data Awal ===")
print(df)

# Membuat pivot table: menghitung rata-rata penjualan per cabang dan bulan
pivot_tbl = df.pivot_table(
    index='Cabang',       # baris: nama cabang
    columns='Bulan',      # kolom: nama bulan
    values='Penjualan',   # nilai yang dihitung
    aggfunc='mean'        # fungsi agregasi: rata-rata
)

print("\n=== Pivot Table (Rata-rata Penjualan) ===")
print(pivot_tbl)