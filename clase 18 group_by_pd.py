import pandas as pd

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')
print(df_books.head(3))

# agrugar los registros por author, media, minimo, maximo, suma
# la llave de la columna que se utiliza es el author se toma como indice 
# print(df_books.groupby('Author').count())
# print(df_books.groupby('Author').mean())
# print(df_books.groupby('Author').max())
# print(df_books.groupby('Author').min())
# print(df_books.groupby('Price').sum())

# print(df_books.groupby('Author').sum().loc['William Davis'])
# print(df_books.groupby('Author').sum().reset_index())

# agg especificas que funciones de agregacion necesitas para el data frame
print(df_books.groupby('Author').agg(['min','max']))

# agrupacion por autor donde pides el maximo de revies y el minimo ademas de la suma de rating
print(df_books.groupby('Author').agg({'Reviews':['min','max'], 'User Rating':'sum'}))

# Agrupar por ‘Author - Year’ y contar los valores de las demás columnas
print(df_books.groupby(['Author','Year']).count())

#Se puede usar las funciones lambda en el método .agg(), para obtener funciones custom ya sea para modificar un valor o para filtrar valores.

print(df_books.groupby('Author').agg({'Year':lambda x: [i-2000 for i in x], 'Reviews':lambda x: sum([i**2 for i in x])}))