import pandas as pd

data = {
    'Cabang': ['A', 'B'],
    'Jan': [100, 80],
    'Feb': [120, 110],
    'Mar': [90, 95]
}

df = pd.DataFrame(data)

# Mengubah dari Wide ke Long format
df_melt = pd.melt(df, 
                  id_vars=['Cabang'], 
                  var_name='Bulan', 
                  value_name='Penjualan')

print(df_melt)