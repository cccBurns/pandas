# Cómo Manipular DataFrames con Pandas en Python
import pandas as pd
import numpy as np

# Creando dos Dataframes de ejemplo
df = pd.DataFrame(np.random.randint(1,10,size=(10, 4)), columns=list('ABCD'))
df1 = pd.DataFrame(np.random.randint(1,10,size=(3, 2)), columns=list('AB'))
df2 = pd.DataFrame(np.random.randint(1,10,size=(3, 2)), columns=list('AB'))
df3 = pd.DataFrame({
    "A": ["Perro", "Gato", "Perro", "Gato", "Perro", "Gato", "Perro", "Gato"],
    "B": ["uno", "uno", "dos", "tres", "dos", "dos", "uno", "tres"],
    "C": np.random.randn(8),
    "D": np.random.randn(8)
})

print(df3)


# Uso de funciones de agregacion sum = suma / mean = media / min = minimo / max = maximo
df_sum = df['A'].mean()
print(df_sum)

# Agrupacion por una columna
grouped_single = df3.groupby('A').sum()
print(grouped_single)

# Agrupacion por varias columnas
grouped_multiple = df3.groupby(['A', 'B']).sum()
print(grouped_multiple)

# Concatenacion de DataFrame
df_concat = pd.concat([df1, df2], axis=0).reset_index(drop=True)
print(df_concat)


""" 
# Uso de funcion agregar
df_agg = df.agg(['sum', 'mean', 'max', 'min', 'count'])
print(df_agg)

print(df1)
print()
print(df2)
print()

# Suma
df_suma = df1 + df2
print(df_suma)

# Resta
df_resta = df1 - df2
print(df_resta)

# Multiplicacion
df_multi = df1 * df2
print(df_multi)

# Division
df_div = df1 / df2
print(df_div)
"""