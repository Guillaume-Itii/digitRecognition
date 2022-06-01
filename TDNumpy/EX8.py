import numpy as np
tab1 = np.random.choice(range(0, 100, 5),20)
tab2 = np.random.choice(range(0, 100, 5),10)

def unique(a,b):
    c = list()
    for i in a:
        if i not in b :
            if i not in c:
                c.append(i)
    c.sort()
    return c

print(tab1)
print(tab2)
print("Fonction crée :",unique(tab1,tab2))
print("Fonction numpy :",np.setdiff1d(tab1,tab2))
