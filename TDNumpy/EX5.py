import numpy as np
tab = np.random.randint(0,100,20)

def minimum(a):
    b = a[0]
    for i in a:
        if i < b:
            b = i
    return b
def maximum(a):
    b = a[0]
    for i in a:
        if i > b:
            b = i
    return b
def indexOf(a,b):
    index = 0
    for i in a:
        if b == i:
            return index
        else:
            index += 1
def moyenne(a):
    total = 0
    for i in a:
        total += i
    return total/len(a)
def plus90(a):
    b = list()
    for i in a:
        if i > 90:
            b.append(i)
    return b
print(tab)
print("1-Minimum :",minimum(tab))
print("1-Index Mini :",indexOf(tab,minimum(tab)))
print("1-Maximum :",maximum(tab))
print("1-Index Maxi :",indexOf(tab,maximum(tab)))
print("1-Moyenne :",moyenne(tab))
print("1-plus de 90 :",plus90(tab))

print(tab)
print("2-Minimum :",tab.min())
print("2-Index :",np.where(tab == tab.min()))
print("2-Maximum :",tab.max())
print("2-Index Maxi:",np.where(tab == tab.max()))
print("2-Moyenne :",np.mean(tab))
print("2-plus de 90 :",tab[tab>90])