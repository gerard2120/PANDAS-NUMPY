import pandas as pd

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',',header=0)

# print(df_books.head(5))

# Aplica pivot_table:
# básicamente, transforma los valores de determinadas columnas o filas en los índices de un nuevo DataFrame, y la intersección de estos es el valor resultante.
# print(df_books.pivot_table(index='Author',columns='Genre',values='User Rating'))
print(df_books.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum'))

# Aplica melt
# toma las columnas del DataFrame y las pasa a filas, con dos nuevas columnas para especificar la antigua columna y el valor que traía.
print(df_books[['Name','Genre']].head(5))

print(df_books[['Name','Genre']].head(5).melt())
# podemos seleccionar las columnas que no quiero hacer melt usando el parámetro id_vars. 
# Para este caso Year y también la única columna que quiero aplicar el melt, para este caso Genre con la propiedad value_var
print(df_books.melt(id_vars='Year',value_vars='Genre'))