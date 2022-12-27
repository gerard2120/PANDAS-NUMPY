import numpy as np
# print()

array = np.arange(0,11)
print(array)

array_copy = array.copy()
trozo_de_array = array[0:6]
print(trozo_de_array)
trozo_de_array[:] = 0
print(trozo_de_array)
print(array_copy)