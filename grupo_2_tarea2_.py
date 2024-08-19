# -*- coding: utf-8 -*-
"""Grupo_2_Tarea2 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hbsh3_um519rQbrUjssYj7OTGo5PXP_V
"""

·import pandas as pd
import numpy as np

#I.
data_ciudades = {
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Habitantes': [1047996, 100169, 92331, 428450, 305717, 484475, 441649, 385098, 294395, 283734],
    'Area_km2': [2672.28, 1545.77, 1487.7, 116.5, 279.89, 6217.26, 368.9, 109.19, 59.4, 483.44],
    'Altitud_m': [154, 2325, 34, 3399, 29, 29, 106, 3271, 562, 156],
    'Densidad_poblacion_por_km2': [3924, 64.8, 62.1, 3673, 1091.6, 77.9, 1196, 3528.6, 4966, 587.2]
}

nfo = pd.DataFrame(data_ciudades)
nfo

#II.
data_ciudades_2 = {
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Gentilicio': ['Limense', 'Arequipeño', 'Trujillano', 'Cusqueño', 'Chiclayano', 'Piurano', 'Iquiteño', 'Huancaino', 'Tacneño', 'Pucallpino'],
    'Provincia': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Maynas', 'Huancayo', 'Tacna', 'Coronel Portillo'],
    'Region': ['Lima', 'Arequipa', 'La Libertad', 'Cusco', 'Lambayeque', 'Piura', 'Loreto', 'Junín', 'Tacna', 'Ucayali']
}
nombres = pd.DataFrame(data_ciudades_2)
nombres

#III.
cuadro_1 = pd.merge(nfo, nombres, on = 'Ciudad', how = 'inner')
cuadro_1

#IV. Mostramos las estadísticas descriptivas principales
cuadro_1.describe()

#Mínimas y Máxima Densidad
min_densidad = cuadro_1['Densidad_poblacion_por_km2'].min()
max_densidad = cuadro_1['Densidad_poblacion_por_km2'].max()
print(min_densidad)
print(max_densidad)

#Ciudades respectivas
ciudad_min_densidad = cuadro_1[cuadro_1['Densidad_poblacion_por_km2'] == min_densidad]['Ciudad'].values[0]
ciudad_max_densidad = cuadro_1[cuadro_1['Densidad_poblacion_por_km2'] == max_densidad]['Ciudad'].values[0]
print(ciudad_min_densidad)
print(ciudad_max_densidad)

#Statement
print(f"La mínima densidad poblacional la tiene {ciudad_min_densidad} con un valor de {min_densidad}.")
print(f"La máxima densidad poblacional la tiene {ciudad_max_densidad} con un valor de {max_densidad}.")

#V. Realizar un gráfico de barras donde se vea la cantidad de habitantes en cada ciudad
import matplotlib.pyplot as plt #importamos librería
#Separamos los datos que queremos
habitantes = cuadro_1['Habitantes']
ciudades = cuadro_1['Ciudad']

fig, ax = plt.subplots(figsize = (12, 6)) #Creamos la base para el gráfico
ax.plot()

ax.bar(x = ciudades, height = habitantes, color ='steelblue') #Ponemos los datos que irán en los ejes

ax.set_xlabel('Ciudad') #Nombramos los ejes
ax.set_ylabel('Habitantes')
ax.set_title('Número de Habitantes por Ciudad de Perú') #Ponemos título al gráfico
ax.tick_params(axis = "x", rotation = 90) #
plt.show()

#VI. Realizar un gráfico de dispersión entre la altura y el número de habitantes en las ciudades del dataframe.
altitudes = cuadro_1['Altitud_m']

fig, ax = plt.subplots(figsize = (10,6))
ax.scatter(altitudes, habitantes, color = 'green')
ax.set_title('Relación entre Altitud y Número de Habitantes de las Ciudades en Perú')
ax.set_xlabel('Altitud (m)')
ax.set_ylabel('Habitantes')
ax.grid(True, alpha=0.5)
plt.show()