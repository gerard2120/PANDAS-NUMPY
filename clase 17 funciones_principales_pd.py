import pandas as pd
import numpy as np

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')
# brinda pequeña informacion, a modo de resumen en el dataframe
print(df_books.info())

# datos utilies a nivel ciencia de datos, media, percentil, min, max etc
print(df_books.describe())

# devuelve los ultimos registros del df
print(df_books.tail(3))

# cuanda memoria usa el df a nivel de columnas o nivel df
print(df_books.memory_usage(deep=True))

# contar las coicidencias de los valores por columnas 
print(df_books['Author'].value_counts())

df_books = df_books.append(df_books.iloc[0])
print(df_books)

df_books = df_books.drop_duplicates()
print(df_books)

# elimina los primeros duplicados pero deja el ultimo
df_books = df_books.drop_duplicates(keep='last')

# Ordenar los registros según valores de la columna (orden ascendente)
print (df_books.sort_values('Year'))

# Ordenar los registros según valores de la columna (orden descendente)
print (df_books.sort_values('Year', ascending=False))