import pandas as pd
import numpy as np

dict = {
    'Col1':[1,2,3,np.nan],
    'Col2':[4,np.nan,6,7],
    'Col3':['a','b','c',None]
}

df = pd.DataFrame(dict)
print(df)
# trae todos los nullos en True
print(df.isnull())
# Convierte lo numero null en 1 y los notNull en 0
print(df.isnull() * 1)
# sustituir valores Null con una palabra o cualquier variable
print(df.fillna('Missing'))
# llenar con la media 
print(df.fillna(df.mean()))
# sustituir valores Null con una serie 
print(df.interpolate())
# borrar todos los datos Nulos
print(df.dropna())
