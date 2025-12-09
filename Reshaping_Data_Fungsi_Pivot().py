import pandas as pd

# 1. Data awal (wide format)
data = {
    'Cabang': ['A', 'B'],
    'Jan': [100, 80],
    'Feb': [120, 110],
    'Mar': [90, 95]
}

df = pd.DataFrame(data)

# 2. Ubah dari Wide -> Long (melt)
df_melt = pd.melt(df, id_vars=['Cabang'], var_name='Bulan', value_name='Penjualan')
print("=== Data Long (df_melt) ===")
print(df_melt)
print()

# 3. Ubah kembali dari Long -> Wide (pivot)
df_pivot = df_melt.pivot(index='Cabang', columns='Bulan', values='Penjualan')
print("=== Data Wide Setelah Pivot (df_pivot) ===")
print(df_pivot)