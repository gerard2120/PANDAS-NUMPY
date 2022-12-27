import numpy as np
lista  = [1,2,3,4,6,7,8,9]
print(lista)
new_list = np.array(lista)
print(new_list)
type(lista)
type(new_list)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mastriz = np.array(matriz)
matriz
# print(matriz)
# indexion, indexado que pueda acceder a los indices
# se accede a la info a nivel de columnas y filas
# se trabaja con estard y end en arrays y matrices 
# Slicing
# La operación de slicing consiste en acceder a la vez a varios elementos de una secuencia mediante los índices. De forma genérica, en una secuencia en Python la sintaxis para realizar la operación es secuencia[i:j], accediendo a los elementos (i,j). La diferenia principal entre las secuencias es el objeto que devuelve la operación de Slicing. En particular, la gran diferencia reside en los arrays de numpy, ya que estos devuelven una vista de los elementos del array original.

# Podemos hacer slice entre índices de la siguiente forma: [start:end]

# Y también podemos definir los pasos, así: [start:end:step]
print(matriz[0])
print(new_list[1:5])
print(new_list[2:])
# pasos en que quieres que se muetren los arreglos
print(new_list[::3])
# acceder a valores desde el final con -1
print(new_list[-1:])
print(new_list[-3:])

print(matriz[1:,0:2])

# clase 03
list1 = list(range(1,10))
# primero dos parametros son el rango de la nueva lista que se espera recibir el tercero son los saltos de la lista que se espera recibir
list2 = np.arange(1,20)
# lista previamente cargada con numeros 0 parametro 1 filas y parametros 2 columnas
list3 = np.zeros(2,3)
# lista previamente cargada con numeros 1 parametro 1 filas y parametros 2 columnas
list4 = np.zeros(2,3)
# lista con 1 parametro de inicio, segundo parametro final, y cuantos datos necesitas ver de esa especificacion
list5 = np.linspace(0,10,20)
# lista para poner una matriz en linea con 1  en diagonal y los demas en 0's
list5 = np.eye(4)
# numero aleatorios y aleatorios n veces
aleatorio = np.random.rand()
aleatorio = np.random.rand(4)
# numeros aleatorios para crear una matriz 4 x 4
aleatorio = np.random.rand(4,4)
# numeros aleatorio entero entre 1 y 15
aleatorio = np.random.rand(1 , 15)
# numeros aleatorio entero entre 1 y 100 llevada a una tupla fija
aleatorio = np.random.rand(1 , 100,(10,10))
