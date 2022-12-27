import pandas as pd
import numpy as np

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')

# filtrado condicional
mayor_a_2016 = df_books['Year'] > 2016
genre_fiction = df_books['Genre'] == 'Fiction'
# print(df_books[mayor_a_2016])
# print(df_books[df_books['Year'] > 2016])
# print(df_books[mayor_a_2016 & genre_fiction])
# negar una condicion sin tener que reescribir con el signo de la ~
print(df_books[~mayor_a_2016])
# filtrae por columna de texto
print(df_books[df_books['Author'].str.contains('Palacio')])
