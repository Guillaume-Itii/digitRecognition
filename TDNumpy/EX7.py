import numpy as np
tabA = np.zeros((5,5)).astype(int)
tabACenter = tabA[1:4,1:4]
tabACenter.fill(5)

tabB = np.zeros((5,5)).astype(int)
tabBCenter = tabB[1:4,1:4]
tabBCenter.fill(5)

np.place(tabB,tabB==0,[1])
np.place(tabB,tabB==5,[0])

print(tabA)
print(tabB)

tabB = np.pad(tabB,1,'constant',constant_values=2)
print(tabB)