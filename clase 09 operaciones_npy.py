import numpy as np
# print()

lista = [1,2]
print(lista)
print(lista * 2)

arr = np.arange(0,10)
arr2 = arr.copy()
print(arr)
print(arr2)

# operaciones
print(arr*2)
print(arr2+2)
# elevar al cuadrado
print(arr**2)

matriz = arr.reshape(2,5)
matriz2 = matriz.copy()
print(matriz)
print(matriz2)
print(matriz * matriz2)
print(matriz - matriz2)
print(matriz + matriz2)

# Una operación importante es la de punto por punto, aquí dos formas de hacerla:
producto_punto = np.matmul(matriz,matriz2.T)
print(producto_punto)

print(matriz @ matriz2.T)