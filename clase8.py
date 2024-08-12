# Cómo Realizar Análisis Exploratorio de Datos con Pandas en Python
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
 
# Ejemplo de DataFrame

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [1, 2, 3, 2, 1]
}) 

print(df)

"""
# Metodo describe
print(df.describe())

# Cuantos valores unicos hay
print(df['C'].nunique())

# Cuantos valores por cada uno de los valores
print(df['C'].value_counts())

# Correlacion de columnas
print(df['A'].corr(df['B']))

# Cov varianza
print(df['A'].cov(df['B']))
"""

correlation_matrix = df.corr()
# Para graficar usamos:
#sns.heatmap(correlation_matrix, annot=True)
#plt.show()

# Grafico de linea
df['C'].plot.line()
plt.show()

# Grafico Histograma
df['A'].plot.hist()
plt.show()

# Grafico con puntos
df.plot.scatter(x='A', y='C')
plt.show()

# Grafico de caja
df['A'].plot.box()
plt.show()

# Grafico de area
df.plot.area()
plt.show()

# Grafico de torta
df['A'].plot.pie()
plt.show()

# Configurar colores en los graficos ej: de lina
df['A'].plot.line(color='red', title='line Plot', xlabel='Index', ylabel='Valor')
plt.show()