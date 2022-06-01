import numpy as np

tab = np.arange(1,26).reshape(5,5).transpose()
print(tab)
print(tab[2:5,1:4])
newTab = tab[[3,1,4]]
print(newTab)
print(newTab[::,[-1,0,1]])
