# Cómo Analizar Estadísticas con Pandas Python

import pandas as pd
import numpy as np

# Creamos un DataFrame con datos de partidos de futbol
df = pd.DataFrame({
    'Equipo': ['Barcelona', 'Real Madrid', 'Atletico', 'Madrid', 'Barcelona', 'Atletico', 'Madrid', 'Barcelona'],
    'Oponentes': ['Atletico', 'Barcelona', 'Madrid', 'Atletico', 'Madrid', 'Barcelona', 'Barcelona', 'Atletico'],
    'Goles anotados': np.random.randint(0, 5, size=8),
    'Goles recibidos': np.random.randint(0, 5, size=8)
})
print(df)

# Creacion de una tabla dinamica
pivot_table = df.pivot_table(values=['Goles anotados', 'Goles recibidos'], index='Equipo', aggfunc=np.sum)
print(pivot_table)

# Agregamos una columna para la diferencia de goles
pivot_table['Diferencia de goles'] = pivot_table['Goles anotados'] - pivot_table['Goles recibidos']
print(pivot_table)

# Usamos la funcion de agregacion mean()
pivot_table = df.pivot_table(values='Goles anotados', index='Equipo', aggfunc=np.mean)
print(pivot_table)