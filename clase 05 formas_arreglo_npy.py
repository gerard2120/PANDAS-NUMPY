import numpy as np
array1 = np.random.randint(1,10, (3,2))
print(array1)
# tamaño de arreglo n x n
print(array1.shape)
array1  = array1.reshape(2,3)
print(array1)

# re ordenar el array y especificando la forma
# ordenar como lenguaje c
# reshape siempre se debe respetar el tamaño de las dimensiones debe de ser igual
array1 = np.reshape(array1,(2,3),'C')
print(array1)

# ordenar como lenguaje fortrant
array1 = np.reshape(array1,(2,3),'F')
print(array1)

# ordenar como lenguaje de optimizar 
array1 = np.reshape(array1,(2,3),'A')
print(array1)