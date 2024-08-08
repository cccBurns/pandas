# Cómo Manejar Datos Faltantes en Python con Pandas

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8], 'C':[9, 10,11,12]})
print(df)

# Comprueba si cada elemento es nulo
print(df.isnull())

# Comprueba si el valor NO es nulo (contrario al anterior)
print(df.notnull())

# Me dice cuantos valos nulos hay por columna
print(df.isnull().sum())

# Elimina filas nulas
df_drop = df.dropna()
print(df_drop)

# Eliminar columnas nulas
df_drop_columnas = df.dropna(axis=1)
print(df_drop_columnas)

# Llenado de datos faltantes con un valor constante (en value= pongo el numero que quiero que ponga)
df_fill = df.fillna(value=0)
print(df_fill)

# Lena los nan con un promedio
df_fill_promedio = df.fillna(df.mean())
print(df_fill_promedio)

# Llenado de datos faltantes usando interpolacion
df_fill_interpolate = df.interpolate()
print(df_fill_interpolate)