import pandas as pd

data = {
    'Cabang': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Penjualan': [100, 150, 200, 250, 300, 350]
}

df = pd.DataFrame(data)
print("=== Data Awal ===")
print(df)
print()

grup = df.groupby('Cabang')
print("=== Data Setelah Grouping ===")
for nama, isi in grup:
    print(f"Cabang {nama}:")
    print(isi)
    print()

hasil = grup['Penjualan'].sum()
print("=== Hasil Summarization ===")
print(hasil)