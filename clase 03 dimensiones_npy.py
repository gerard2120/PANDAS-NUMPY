import numpy as np
# saber el numero de dimensiones en numpy
scalar = np.array(21)
print(scalar)
print(scalar.ndim)

vector = np.array([1,2,3])
print(vector)
print(vector.ndim)

matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.ndim)

tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[13, 13, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
print(tensor)
print(tensor.ndim)

# agregar/eliminar dimensiones
vector1 = np.array([1,2,4],ndmin=10)
print(vector1)
print(vector1.ndim)

#
# axis 0 es filas y axis 1 son las columnas
vector2 = np.expand_dims(np.array([1,2,4]), axis=0)
print(vector2)
print(vector2.ndim)

# comprime el vector a la dimension correcta que deberia tener
vector1 = np.squeeze(vector1)
print(vector1, vector1.ndim)