import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Crear un grafico de barras a partir de la tabla dinamica
pivot_table['Diferencia de goles'].plot(kind='bar')
plt.ylabel('Diferencia de goles')
plt.show()

# DataFrame con datos de partidos
df2 = pd.DataFrame({
    'Equipo': ['Barcelona', 'Real Madrid', 'Atletico'] * 3,
    'Partido': ['Partido' + str(i) for i in range(1, 9)],
    'Goles anotados': np.random.randint(0, 5, size=9),
    'Goles recibidos': np.random.randint(0, 5, size=9)
})
print(df2)