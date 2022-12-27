import pandas as pd
# print()

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')

# slicing mas avanzado se hace mediante loc y iloc
print(df_books[0:4])
# por el nombre de la columna
print(df_books['Name'])
print(df_books[['Name','Author','Year']])
# trae los datos del dataframe del 0 al 4, incluyendo al 4
print(df_books.loc[0:4])
# mas los nombres de las columnas
print(df_books.loc[0:4, ['Name','Author']])
# multiplicar solo los valores filtrados por el loc del label
print(df_books.loc[0:4, ['Reviews']] * -1)
# multiplicar solo los valores filtrados por el loc del label
print(df_books.loc[0:4, ['Author']] == 'JJ Smith' )
# el primer valor es el row, el segundo la columna
# iloc no necesitas saber el nombre de las columnas es especificamente por el indice del dataframe
print(df_books.iloc[:,0:3] )
# valor especifico con iloc el primer parametro la row y el segundo la columna de 0 sin contar el indice
print(df_books.iloc[1,3] )
print(df_books.iloc[1,3] * -1 )
print(df_books.iloc[:2,2:])