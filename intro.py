import pandas as pd

serie = pd.Series([1,2,3,4,5,6,7,8,9,])

#print(serie)

datos = {
    'nombre': ["Ana", "Ivan", "Carlos"],
    'edades': [25, 31, 36]
}

df = pd.DataFrame(datos)

print(df)