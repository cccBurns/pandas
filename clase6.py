# Cómo Ordenar y Hacer Ranking en DataFrames de Pandas Python
import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Belen', 'Ivan'],
    'Edad': [32,28,15,56,28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Arica']
}

df = pd.DataFrame(data)
print(df)

# Ordenar por columna Edad (de menos a mayor)
df = df.sort_values(by='Edad')
print(df)

# Ordenar por columna (de mayor a menor)
df = df.sort_values(by='Edad', ascending=False)
print(df)

# Ordenar por multiples columnas (con reset_index() reseteamos los id)
df = df.sort_values(by=['Ciudad', 'Edad']).reset_index(drop=True)
print(df)

# Ordenar por indice (con ascending=False lo pone de mayor a menor)
df = df.sort_index(ascending=False)
print(df)

# Crear un ranking basico
df['Ranking_Edad'] = df['Edad'].rank()
print(df)

#

