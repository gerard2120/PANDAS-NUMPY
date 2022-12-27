import numpy as np
# print()
array = np.random.randint(1,20,10)
print(array)

matriz = array.reshape(2,5)
print(matriz)

# muestra el valor maximo
print(array.max())
print(array.argmax())
print(array.argmax())

print(matriz.max())
print(matriz.argmax(0))
print(matriz.argmax(1))

# muestra el valor minimo
print(array.min())
print(array.argmin())

print(matriz.argmin(0))
print(matriz.argmin(1))

# diferencia entre el pico mas bajo al pico mas alto
print(array.ptp())
# distancia determinado eje por ejemplo eje 0
print(matriz.ptp(0))
# especifica el percentil que estes trabajando
# percentil es el valor que se encuentra en la mitad
print(np.percentile(array, 50))
# sort, ordena de mayor a menor los numeros que se tienen en mi arreglo
print(array.sort())
# la mediana de un array
print(np.median(array))
print(np.median(array))
print(np.median(array, 0))

# desviacion estandar 
print(np.std(array))

# varianza 
print(np.var(array))
# media estadistica
print(np.mean(array))
# concatenar 
a = np.array([[1,2],[3,4]])
print(a)
b = np.array([5,6])
b = np.expand_dims(b, axis=0)
print(b)
c = np.concatenate((a,b), axis=0)
print(c)
# te mayuscula es la transpuesta de una matriz para distribuir correctamente la matriz
d = np.concatenate((a,b.T), axis=1)
print(d)