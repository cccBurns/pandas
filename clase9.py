# Cómo trabajar con fechas y tiempo en Python y Pandas
from datetime import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Convertir cadena de texto a datetime
#fecha_str = '2023-01-01 10:00:00'
#fecha_dt = pd.to_datetime(fecha_str)
#print(fecha_dt)
#print(fecha_str)

# Creando un objeto Timestamp en Pandas
#timestamp = pd.Timestamp(datetime.now())
#print(timestamp)

# Creando un DatetimeIndex en Pandas
meses = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
print(meses)

#dias = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
#print(dias)

# Creacion de series de tiempo
serie = pd.Series(np.random.randn(len(meses)), index=meses)
print(serie)

serie_diaria = pd.Series(np.random.randn(90), index=pd.date_range(start='2023-01-01', end='2023-03-31', freq='D'))
print(serie_diaria)

# Desplazamiento o "shifting"
serie_shifted = serie.shift(1)
print(serie_shifted)

# Cambio de frecuencia a datos mensuales con asfreq
serie_mensual = serie_diaria.asfreq('M')
print(serie_mensual)

# Remuestreo de datos diarios en datos mensuales con resample
serie_resample = serie_diaria.resample('M').mean()
print(serie_resample)

# Asignando una zona horaria
serie_tiempo_tz = serie_diaria.tz_localize('UTC')
print(serie_tiempo_tz)

# Convertir a otra zona horaria
serie_tiempo_tz_ny = serie_tiempo_tz.tz_convert('America/New_York')
print(serie_tiempo_tz_ny)

# Saber cuales son las zonas horarias disponible
import pytz
for tz in pytz.all_timezones:
    print(tz)
    
# Crear un objeto period
periodo = pd.Period('2023-01')
print(periodo)

# Creando un objeto period
periodo = pd.Period('2023-01-01')
print(periodo)

# agregar un periodo
periodo1 = periodo + 1
print(periodo1)

# Sumar fecha

timestamp = pd.Timedelta(datetime.now())
print(timedelta)
delta = timedelta(days=7)
print(delta)
nueva_fecha = timestamp + delta
print(nueva_fecha)

# Creando un DF con una columna de fechas en formato texto
df = pd.DataFrame({'fecha': ['2023-01-01', '2023-01-02', '2023-01-03'],
                   'valor': [1, 2, 3]})
# Comvertir la columna de fechas a datetime
df['fecha'] = pd.to_datetime(df['fecha'])
print(df)

# Suponiendo que precios es nuestra serie de tiempo de precios de cierre diarios
precios = pd.Series(np.random.rand(100), index=pd.date_range(start='2023-01-01', periods=100, freq='D'))
print(precios)
# Calcular la media movil de las ultimos 7 dias
media_movil = precios.rolling(window=7).mean()
print(media_movil.head(7))

# Trazar la serie de tiempo de precios y la media movil
plt.figure(figsize=(12,6))
precios.plot(label='Precio de cierre')
media_movil.plot(label='Media movil de 7 dias')
plt.title('Precio de cierre y media movil de 7 dias')
plt.legend()
plt.show()