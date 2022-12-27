import pandas as pd
import numpy as np

# Join es un index match
izq = pd.DataFrame({'A': ['A0','A1','A2'],
  'B':['B0','B1','B2']},
  index=['k0','k1','k2'])

der =pd.DataFrame({'C': ['C0','C1','C2'],
  'D':['D0','D1','D2']},
  index=['k0','k2','k3'])
 
print(izq)
print(der)

# el join por default es el left join
# print(izq.join(der))


# inner join
print(izq.join(der, how='inner'))

# inner join
print(izq.join(der, how = 'outer'))