import pandas as pd

datos = {
    "Nombre":['Ana', 'Ivan', 'Pedro', 'Angela'],
    "Edad": [27,23,56,32]
}



datos2 = [{'Nombre': 'Ana', 'Edad':27},
          {'Nombre': 'Ivan', 'Edad':23},
          {'Nombre': 'Pedro', 'Edad':56},
          {'Nombre': 'Angela', 'Edad':32},
          ]
# Agregar una columna Nacionalidad
df2 = pd.DataFrame(datos2)
df2["Nacionalidad"] = ["chilena", "chileno", "Argentino", "Española"]

#Cambiar orden de columnas
df2 = df2[["Edad", "Nacionalidad", "Nombre"]]
#print(df2)

# Crear nueva fila
nueva_fila = pd.DataFrame({'Nombre':'Daniela', 'Edad':29, 'Nacionalidad':'Colombiana'}, index = [4])
df2 = pd.concat([df2, nueva_fila])

print(df2)