import numpy as np
A = np.random.randint(10,20,size=(3,3))
B = np.random.randint(10,20,size=(3,3))

def sommeDiagonale(a,b):
    tot = 1
    tot *= a[0][0] + b[0][0]
    tot *= a[1][1] + b[1][1]
    tot *= a[2][2] + b[2][2]

    return tot

print(A+B)
print(A*B)

print(A.dot(B))
#La difference est que l'opérateur * est qu'il multiplie A[x][y] à B[x][y] alors que dot() effectue le produit matriciel
print("Somme diagonale :",sommeDiagonale(A,B))

