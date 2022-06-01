import numpy as np

tab1d = np.linspace(0,98)

print(tab1d)
print("Dimension :" , tab1d.ndim)
print("Dimension :" , len(tab1d))

tab1d = tab1d.reshape(5,10)

print(tab1d)
print("Dimension :" , tab1d.ndim)
print("Dimension :" , len(tab1d))