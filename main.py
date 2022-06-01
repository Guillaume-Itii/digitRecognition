from skimage import io
import numpy as np
from math import pow

def imgToTxt(img,file):
    destination = open(file+".txt", "w")
    for row in img:
        np.savetxt(destination, row)
    destination.close()

def img2gray(img):
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    return R * 0.2125 + G * 0.7154 + 0.0721 * B

def blackWhite(img):
    img[img >= 90] = 255
    img[img < 90] = 0
    return img

def filter(img, n):
    for k in range(n, len(img) - n):
        for i in range(n, len(img[0]) - n):
            m = 0
            for x in range(k - n, k + n + 1):
                for y in range(i - n, i + n + 1):
                    m += img[x, y]
            img[k, i] = m / pow(2 * n + 1, 2)
    return img


img = blackWhite(filter(blackWhite(img2gray(io.imread('horloge1.jpg'))), 3))

# imgToTxt(img,"test")
# print(img.shape)
# print(img)

x_coord = 0
y_coord = 0

for y in range(0 ,len(img)):
    for x in range(0,len(img)):
        if img.item(y,x) == 255 :
            if x_coord == 0 and y_coord == 0:
                x_coord = x
                y_coord = y

print("first x : " + str(x_coord))
print("first y : " + str(y_coord))

digit = img[y_coord-10:y_coord+110,x_coord-25:x_coord+50]


print(digit)

io.imshow(digit, cmap='gray')
io.show()
