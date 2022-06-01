import numpy as np
tab = np.random.randint(0,100,10)

tab2d = np.random.randint(0,100,size=(5,5))

def tri(t):
    for i in range(1,len(t)):
        temp=t[i]
        j=i
        while j>0 and temp<t[j-1]:
            t[j]=t[j-1]
            j-=1
        t[j]=temp
    return t
def index(a,b):
    c = list()
    for i in b:
        c.append(np.where(a == i)[0])
    return c
tab_trier = tab.copy()
tab_trier = tri(tab_trier)

print(tab)
print(tab_trier)
print("Index :",index(tab,tab_trier))
print(tab2d)
tab2d = tab2d.argsort()
print(tab2d)
