import numpy as np
from sympy import *

tab = np.arange(2,1001)
tab2 = np.empty(0)
e=0
for i in range (len(tab)):
    isprime(i)
    if isprime(i) == True :
        tab2=np.append(tab2,i)
        e=e+1
print(tab2)
print(e)