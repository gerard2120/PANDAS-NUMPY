import numpy as np
# se puede cambiar el tipo de dato agregando el type al momento de crear las variables
array = np.array([1,2,3,4], dtype='float64')
# saber que tipo de dato es 
print(array.dtype)
print(array)
# cambiar el tipo de dato sobre ejecucion
array = array.astype(np.float32)
print(array.dtype)
array = array.astype(np.bool_)
print(array.dtype)
array = array.astype(np.string_)
print(array.dtype)
array = array.astype(np.int32)
print(array.dtype)