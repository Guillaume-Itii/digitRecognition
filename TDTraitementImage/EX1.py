from skimage import io
import numpy as np

PARTIE = 2

def printImg(img,type="rgb"):
    if type == "rgb":
        # print("Affichage RGB")
        io.imshow(img)
        io.show()
    elif type == "gray":
        # print("Affichage gris")
        io.imshow(img, cmap="gray")
        io.show()
def img2gray(img):
    if imgMode(img.ndim) == "RGB":
        # t = list()
        # for j in range(len(a)):
        #     for k in range(len(a[0])):
        #         t.append( int(0.2125 * a[j][k][0] + 0.7154 * a[j][k][1] + 0.0721 * a[j][k][2]))
        # t = np.reshape(t,(a.shape[0],a.shape[1]))
        R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        t = R * 0.2125 + G * 0.7154 + 0.0721 * B
        return t
    else :
        print("Mauvais format")
        return "Mauvais format"

def imgMode(a):
    # print(a)
    if a == 1:
        return "B&W"
    elif a == 2:
        return "gray"
    elif a == 3:
        return "RGB"
    elif a == 4:
        return "RGBA"
    else:
        return "ERREUR DE FORMAT"

def addBorder(img,b,type="rgb",value=0):
    if(type=="rgb"):
        return np.pad(img2gray(img),b,'constant',constant_values=value)
    elif(type=="gray"):
        return np.pad(img, b, 'constant', constant_values=value)
    else:
        return "Erreur"
def flipImage(img,side="horizontal"):
    if side == "horizontal":
        return np.flip(img,0)
    elif side == "vertical":
        return np.flip(img,1)
def intToImage(n):
    numberList = img2gray(io.imread('number.jpg'))
    spaces = 1
    print(numberList.shape)
    if n == 0:
        return numberList[:,:135]
    elif n == 1:
        return numberList[:,spaces*n:spaces*(n+1)]


printImg(intToImage(0),type="gray")
printImg(intToImage(1),type="gray")
printImg(intToImage(2),type="gray")
printImg(intToImage(3),type="gray")
printImg(intToImage(4),type="gray")
printImg(intToImage(5),type="gray")
printImg(intToImage(6),type="gray")
printImg(intToImage(7),type="gray")
printImg(intToImage(8),type="gray")
printImg(intToImage(9),type="gray")
# printImg(img)
#
# print("Type :", type(img))
# print("Type de valeur :", type(img[0][0][0]))
# print("Nombre de valeurs :", img.size )
# print("Dimension :", img.ndim)
# print("Mode :", imgMode(img.ndim))
# print("Forme :", img.shape)
#
# printImg(img2gray(img),type="gray")
# printImg(addBorder(img,25,type="rgb"),type="gray")
# printImg(flipImage(img2gray(img),side="vertical"),type="gray")
# printImg(flipImage(img2gray(img),side="horizontal"),type="gray")