# Cómo Aplicar Funciones y Manipular Datos en Pandas Python

import pandas as pd

data = {'nombre': ['Matoas Fernandez', 'Salma Hayek', 'Alexis Sanchez', 'Sofia Vergara'],
        'edad': [25, 30, 35, 40],
        'ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

df = pd.DataFrame(data)
print(df)

df['edad'] = df['edad'].apply(lambda x: x + 5)

def convertir_a_mayusculas(x):
    return x.upper()
df['nombre'] = df['nombre'].apply(convertir_a_mayusculas)

promedio_edad = df['edad'].mean()
print(promedio_edad)

df['nombre'] = df['nombre'].replace('Matias Fernandez', 'Jorge Valdivia')

print(df)