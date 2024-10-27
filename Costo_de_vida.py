# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:52:14 2024

@author: Joel Olguin Lopez
"""

import pandas as pd
import matplotlib.pyplot as plt
datos= pd.read_csv('living.csv') # Abre el archivo CSV o excel
print(datos.head()) #Devuelve las primeras 5 filas
print(datos.info())  # Mostramos el data frame

#Numero de columnas y de filas 
num_filas, num_columnas = datos.shape
print(f'Número de filas: {num_filas}')
print(f'Número de columnas: {num_columnas}')

# Costo de vida promedio
promedio_cost_vida = datos['Cost of living, 2017'].mean()
print(f"El promedio del costo de vida es: {promedio_cost_vida}")

#Pais con costo de vida más alto 
pais_cost_alto = datos.loc[datos['Cost of living, 2017'].idxmax()]['Countries']
print(f"El pais con el costo de vida mas alto es: {pais_cost_alto}")

#Pais con costo de vida más bajo
pais_cost_bajo = datos.loc[datos['Cost of living, 2017'].idxmin()]['Countries']
print(f"El pais con el costo de vida mas bajo es: {pais_cost_bajo}")

#Costo de vida en Perú
costo_vida_peru = datos.loc[datos['Countries'] == 'Peru', 'Cost of living, 2017'].values[0]
print(f"El costo de vida en peru es: {costo_vida_peru}")

#Ranking de Perú
ranking_peru = datos.loc[datos['Countries'] == 'Peru', 'Global rank'].values[0]
print(f"El ranking de peru es: {ranking_peru}")

#10 países con el costo de vida más alto 
print(f"LOS 10 PAISES CON EL COSTO DE VIDA ALTO")
paises_altos = datos.nlargest(10, 'Cost of living, 2017')
print(paises_altos)

#10 psíses con el costo de vida mas bajo 
print(f"LOS 10 PAISES CON EL COSTO DE VIDA BAJO")
paises_bajos = datos.nsmallest(10, 'Cost of living, 2017')
print(paises_bajos)

#El costo de vida de los países de America
paises_america =  datos.loc[datos['Continent'] == 'America']

costo_vida_america = paises_america.groupby(['Continent'])['Cost of living, 2017'].sum().values[0]
print(f"El costo de vida de los paises de America es: {costo_vida_america}")

