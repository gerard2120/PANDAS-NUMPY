import numpy as np

array = np.linspace(1,10,10, dtype='int8')
print(array)

print(array > 5)

print(array[(array > 5) & (array < 9)] )

array[array>5]= 99
print(array)

# Otra funcion muy util de numpy tambien es np.where(condicion, valor si, valor si la condicion no se cumple), ejemplo:
matriz = np.array([[19,  4, 43],[ 8, 96, 80],[ 6, 99, 35]])
matriz = np.where(matriz > 50, 0, 1)

print(matriz)