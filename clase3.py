# Cómo Importar y Exportar Datos con Pandas en Python

import pandas as pd

# Cargar un archivo CSV completo
#df = pd.read_csv('banco.csv')
#print(df)

# Como seleccionar un CSV con seleccion de columnas
#df = pd.read_csv('banco.csv', usecols=['Surname', 'CreditScore', 'EstimatedSalary', 'Card Type'])
#print(df)

# Cargar datos desde un archivo HTML
df = pd.read_html('https://campeonatochileno.cl/estadisticas',)[0]
#print(df)

# Exportar un DataFrame completo a CSV
#df.to_csv('datos.csv', index=False)
#print(df)

# Exportar un DataFrame a CSV con seleccion de columnas
#df[['Pos', 'Club', 'PTS']].to_csv('datos.csv', index=False, encoding='utf-8-sig')
#print(df)

# Exportar un DataFrame completo a Excel con nombre
df.to_excel('datos.xlsx', index=False, sheet_name='Torneo Chileno')
print(df)