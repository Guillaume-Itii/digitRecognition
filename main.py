import numpy as np
from skimage import io

def imgToTxt(img,file):
    destination = open(file+".txt", "w")
    for row in img:
        np.savetxt(destination, row)
    destination.close()

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

def img2gray(img):
    if imgMode(img.ndim) == "RGB":
        R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        t = R * 0.2125 + G * 0.7154 + 0.0721 * B
        return t
    else :
        print("Mauvais format")
        return "Mauvais format"

img = io.imread('horloge1.jpg')
gray = img2gray(img)

print(img.shape)
print(gray.shape)
print(gray)

imgToTxt(img,"imageStandard")
imgToTxt(gray,"imageGray")