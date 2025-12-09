import pandas as pd
import matplotlib.pyplot as plt

# Membuat data
data = {
    'Bulan': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06', 
              '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12'],
    'Penjualan': [120, 135, 150, 160, 170, 180, 175, 190, 200, 210, 220, 230]
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Hitung rata-rata bergerak 3 bulan
df['MA_3'] = df['Penjualan'].rolling(window=3).mean()

# Plot hasil
plt.figure(figsize=(8,4))
plt.plot(df.index, df['Penjualan'], label='Penjualan Asli', marker='o')
plt.plot(df.index, df['MA_3'], label='Rata-rata Bergerak (3 bulan)', linestyle='--')
plt.title('Analisis Tren Penjualan')
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.legend()
plt.show()