import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data penjualan bulanan
data = {
    'Bulan': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06', 
              '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12'],
    'Penjualan': [120, 135, 150, 160, 170, 180, 175, 190, 200, 210, 220, 230]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Tambahkan indeks waktu (0-11)
df['time_index'] = np.arange(len(df))

# Pisahkan fitur dan target
X = df[['time_index']]
y = df['Penjualan']

# Buat dan latih model regresi Linear
model = LinearRegression()
model.fit(X, y)

# Prediksi bulan ke-13 (index ke-12)
next_month = np.array([[12]])
prediksi_bulan13 = model.predict(next_month)[0]
print(f"Prediksi penjualan bulan ke-13: {prediksi_bulan13:.2f}")

# Buat data prediksi untuk semua bulan termasuk bulan ke-13
X_all = np.arange(0, 13).reshape(-1, 1)
y_pred_all = model.predict(X_all)

# Visualisasi hasil
plt.figure(figsize=(9,5))
plt.plot(df['time_index'], y, label='Data Aktual', marker='o')
plt.plot(X_all, y_pred_all, label='Tren Linear (Prediksi)', linestyle='--', color='orange')
plt.scatter(12, prediksi_bulan13, color='red', label=f'Prediksi Bulan ke-13 = {prediksi_bulan13:.2f}')
plt.title('Prediksi Tren Penjualan dengan Linear Regression')
plt.xlabel('Bulan ke-')
plt.ylabel('Penjualan')
plt.legend()
plt.grid(True)
plt.show()