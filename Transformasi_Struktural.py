import pandas as pd

data = {
    'ID_Pelanggan': [1, 2, 3],
    'Nama_Lengkap': ['Andi Saputra', 'Budi Santoso', 'Citra Dewi'],
    'Tanggal': ['2025/11/01', '2025/11/02', '2025/11/03']
}

df = pd.DataFrame(data)


df[['Nama_Depan', 'Nama_Belakang']] = df['Nama_Lengkap'].str.split(' ', n=1, expand=True)

# Pengubahan format tanggal
df['Tanggal'] = pd.to_datetime(df['Tanggal']).dt.strftime('%d-%m-%Y')

print(df)