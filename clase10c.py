import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataframe con datos de partidos
df = pd.DataFrame({
    'Equipo': ['Barcelona', 'Real Madrid', 'Atletico'] * 3,
    'Partido': ['Partido' + str(i) for i in range(1, 10)],
    'Goles anotados': np.random.randint(0, 5, size=9),
    'Goles recibidos': np.random.randint(0, 5, size=9)
})
print(df)

# Uso del metodo melt en datos de partidos
df_melted = df.melt(id_vars=['Equipo', 'Partido'], value_vars=['Goles anotados', 'Goles recibidos'])
print(df_melted)

# Creamos un DataFrame con los goles anotados por los jugadores en diferentes partidos
df = pd.DataFrame({
    'Partido': ['Partido 1', 'Partido 2', 'Partido 3'],
    'Messi': [2, 1, 0],
    'Ronaldo': [1, 0, 2],
    'Neymar': [0, 2, 1]
})
print(df)

# Convertir el DataFrame  a formato "long" usando el metodo melt
df_melted = df.melt(id_vars='Partido', value_vars=['Messi', 'Ronaldo', 'Neymar'], var_name='Jugador', value_name='Goles anotados')
print(df_melted)


# Sumar los goles anotados por cada jugador
goles_por_jugador = df_melted.groupby('Jugador')['Goles anotados'].sum()
print(goles_por_jugador)


