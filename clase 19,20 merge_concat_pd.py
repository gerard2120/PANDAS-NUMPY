import pandas as pd
import numpy as np

df_1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
  'B':['B0','B1','B2','B3'],
  'C':['C0','C1','C2','C3'],
  'D':['D0','D1','D2','D3']
})

df_2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
  'B':['B4','B5','B6','B7'],
  'C':['C4','C5','C6','C7'],
  'D':['D4','D5','D6','D7']
})

# concatenamos por default en axis 0, y para evitar los indices le damos ignore_index = True
# print(pd.concat([df_1,df_2], ignore_index=True))
# concatenacion de manera vertical por axis 1
# print(pd.concat([df_1,df_2], axis=1))

# Merge 
izq = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
    'A' : ['A0', 'A1', 'A2','A3'],
    'B': ['B0', 'B1', 'B2','B3']})

der = pd.DataFrame({'key_2' : ['k0', 'k1', 'k2',np.nan],
    'C' : ['C0', 'C1', 'C2','C3'],
    'D': ['D0', 'D1', 'D2','D3']})

print(izq)
print(der)
# join entra por las llaves de entrada
# print(izq.merge(der, on='key'))

# especificas el metodo de entrada de join para las dos columnas
# 
print(izq.merge(der, left_on='key', right_on='key_2'))

# how especificas la union de merge, es decir lef, rigth, outer, inner join
print(izq.merge(der, left_on='key', right_on='key_2', how='left'))