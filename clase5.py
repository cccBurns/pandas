# Cómo Aplicar Funciones y Manipular Datos en Pandas Python

import pandas as pd

data = {'nombre': ['Matias Fernandez', 'Salma Hayek', 'Alexis Sanchez', 'Sofia Vergara'],
        'edad': [25, 30, 35, 40],
        'ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

# Transformo los datos de arriba a DF
df = pd.DataFrame(data)
print(df)

# El metodo apply le aplica una funcion a una columna del DF, en este caso a la columna Edad
#df['edad'] = df['edad'].apply(lambda x: x + 5)
#print(df)

# Pasar nombres a mayusculas
#def convertir_a_mayusculas(x):
#    return x.upper()
#df['nombre'] = df['nombre'].apply(convertir_a_mayusculas)
#print(df)

# Imprime el promedio de la edad (.mean = pronmedio, .sum = suma, .max = maximo, .min = minimo,)
#promedio_edad = df['edad'].mean()
#print(promedio_edad)

# Reemplazar nombre, primero el elemento que quiero reemplazar y despues por el cual quiero que se reemplace
df['nombre'] = df['nombre'].replace('Matias Fernandez', 'Jorge Valdivia')
print(df)

# Reemplazar varios nombres
df['nombre'] = df['nombre'].replace(['Matias Fernandez', 'Salma Hayek'], ['Jorge Valdivia', 'Jenna Ortega'])
print(df)

# Reemplazar todos los nombres que empiecen con A
df['nombre'] = df['nombre'].replace(r'^A.*', 'Anonimo', regex=True)
print(df)

# Separar una columna en dos
df[['nombre', 'apellido']] = df['nombre'].str.split(' ', expand=True)
print(df)