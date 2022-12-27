import pandas as pd
import numpy as np
# print()
df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')
# muestra los primero datos del dataframe
# print(df_books.head(3))
# eliminar columnas de un dataframe por medio de su cabecera, con dro solo lo borra de la salida
# print(df_books.drop('Genre', axis=1).head(3))
# print(df_books.head(3))
# eliminar la columna del dataframe directo por medio de su cabecera
# print(df_books.drop('Genre', axis=1, inplace=True))
# print(df_books.head(3))
df_books = df_books.drop('Year', axis=1)
# print(df_books.head(3))

del df_books['Price']
# print(df_books.head(3))
# borrado de toda la fila 
# print(df_books.drop(0,axis=0).head(3))
# borrado con una lista 
# print(df_books.drop([0,1,2],axis=0).head(3))
# borrado utilizando un rango con una tupla
# print(df_books.drop(range(0,10),axis=0).head(3))

print(df_books.head(3))

# se crea nueva cplumna con Nan
df_books['Nueva_Columna'] = np.nan
print(df_books.head(3))

# print(df_books.shape[0])
# print(np.arange(0,df_books.shape[0]))
data = np.arange(0,df_books.shape[0])
# print(data)
df_books['Rango'] = data
print(df_books.head(10))
# agregar registros a nivel de filas 
df_books.append(df_books)