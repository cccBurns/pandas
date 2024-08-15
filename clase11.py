# Ejemplo de cómo Analizar un Conjunto de Datos del Titanic

import pandas as pd

file_path = 'Titanic-Dataset.csv'
df = pd.read_csv(file_path)

# Ver las primeras 5 filas del DataFrame
print(df.head())

# Obtener informacion sobre el DataFrame
print(df.info())

# Limpieza de lo datos
# Verificar si hay valores nulos
print(df.isnull().sum())
# Eliminar filas con valores nulos
df = df.dropna().reset_index(drop=True)

# Verificar si hay duplicados
print(df.duplicated().sum())
# Eliminar duplicados
df = df.drop_duplicates()

print(df)

# Conversion de tipos de datos
df['Age'] = df['Age'].astype(int)

# Creacion de nuevas columnas
df['Tamaño Familia'] = df['SibSp'] + df['Parch']

# Ordenamiento de datos
df_sorted = df.sort_values(by='Age')
print(df_sorted)

# Aplicar funciones estadisticas
print(df['Age'].mean())
print(df['Fare'].max())

# Visualizacion de datos
import matplotlib.pyplot as plt

df['Age'].hist(bins=30)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Creacion de resumenes de datos
summary = df.describe()

# Exportacion de los resultados
summary.to_csv('summary.csv')

# Categorizar la edad
def categorize_age(age):
    if age < 18:
        return 'Niño'
    elif age < 60:
        return 'Adulto'
    else:
        return 'Anciano'
    
df['Categoria Edad'] = df['Age'].apply(categorize_age)
print(df)

survived_df = df[df['Survived'] == 1].reset_index(drop=True)

mean_age_by_class = df.groupby('Pclass')['Age'].mean()
print(mean_age_by_class)

pivot_table = df.pivot_table(index='Sex', columns='Pclass', values='Fare', aggfunc='mean')
print(pivot_table)
