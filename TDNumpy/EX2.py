import numpy as np

tab2d = np.ones((10,10)).astype(int)
print("Tableau de base :")
print(tab2d)

#tab2d = tab2d.reshape(-1)

tab2d[0::2,0::2].fill(0)
tab2d[1::2,1::2].fill(0)

print("Tableau de 1 et 0 :")
print(tab2d)

