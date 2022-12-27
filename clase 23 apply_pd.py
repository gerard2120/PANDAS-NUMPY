import pandas as pd

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',',header=0)

print(df_books.head(5))

# Apply es un comando muy poderoso que nos deja aplicar funciones a nuestro DataFrame
def two_times(value):
    return value * 2
# cada fila que recorre una de las filas aplica la funcion creada
print(df_books['User Rating'].apply(two_times))

print(df_books['User Rating'].apply(lambda x : x * 3))

# se especifica a nivel columna
print(df_books.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1))