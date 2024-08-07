import pandas as pd


banco = pd.read_csv('banco.csv')
#print(banco.columns)

peliculas = pd.read_excel('peliculas.xlsx')
#print(peliculas.columns)

df_vacio = pd.DataFrame()

#print(banco["Geography"])

columnas_enteras = peliculas.select_dtypes(include='object')
#print(columnas_enteras.columns)

peliculas["Actor Principal"] = "Leo di Caprio"

# eliminar una columna con drop
peliculas = peliculas.drop("Actor Principal", axis = 1)

# Imprimir las primeras 4 columnas
primeras_4 = peliculas.iloc[:, :4]

# Imprimir las primeras 4 filas
#print(primeras_4.columns)

# Seleccionar la primera fila de banco
#print(banco.iloc[0])

peliculas_mayor_a_7 = peliculas[peliculas['vote_average'] > 7]
print(peliculas_mayor_a_7['vote_average'])