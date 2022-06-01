import numpy as np
tab = np.random.randint(1,10,size=(10,10))
tab2 = np.zeros((10,10))
print(tab)
u, c = np.unique(tab, return_counts=True)

d = dict(zip(u,c))

print(d)