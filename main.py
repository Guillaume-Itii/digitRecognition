from skimage import io
import numpy as np
from math import pow
import matplotlib.pyplot as plt
import matplotlib
import pictCutter as pc

matplotlib.rcParams["font.size"] = 18

# Charge dans un tableau des chiffres préconstruit dans des TXT
def loadDigitTab():
    digitList = []
    for i in range(0, 10):
        digitList.append(np.loadtxt('./digitDB/' + str(i) + '.txt', delimiter=','))
        # print("-----Digit : " + str(i) + "-----")
        # print(digitList[i])
    return digitList


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


def getDigit(img):
    x_coord = 0
    y_coord = 0

    for y in range(0, len(img)):
        for x in range(0, len(img)):
            if img.item(y, x) == 255:
                if x_coord == 0 and y_coord == 0:
                    x_coord = x
                    y_coord = y

    digit = img[y_coord - 2:y_coord + 110, x_coord - 20:x_coord + 50]

    return digit


# Redimensionne une image (digit_created) par rapport a la taille d'une autre (digit_found)
def resize(digit_found, digit_created):
    C = digit_created

    w, h = C.shape[:2]

    xNew = np.shape(digit_found)[0]
    yNew = np.shape(digit_found)[1]

    xScale = xNew / (w - 1)
    yScale = yNew / (h - 1)

    newImage = np.zeros([xNew, yNew, 1])

    for i in range(xNew - 1):
        for j in range(yNew - 1):
            newImage[i + 1, j + 1] = C[1 + int(i / xScale),
                                       1 + int(j / yScale)]
    return newImage

# Affiche deux images
def showBothPict(a, b):
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()
    ax[0].imshow(a)
    ax[1].imshow(b)
    fig.tight_layout()
    plt.show()

# Compare l'image passé en paramètre avec la liste tiré de la base de donnée de chiffre
def compareWithStandard(digit_found, digitList):
    min_error = 1
    number_mermory = 0
    for i in range(0, len(digitList)):
        digit_created = resize(digit_found, digitList[i])[:, :, 0]

        error = np.mean(digit_found != digit_created)
        percent = (1 - error) * 100

        if error < min_error:
            min_error = error
            number_mermory = i

        print("Taux d'erreur pour " + str(i) + " : " + str(error))
        print("Taux de ressemblance pour " + str(i) + " : " + str(percent))

    print("Taux retenu : " + str(min_error))
    print("Chiffre potentiel : " + str(number_mermory) )

    showBothPict(digit_found, digitList[number_mermory])
    return number_mermory

# Charge la liste de digit préconstruite
digitList = loadDigitTab()

# Transforme une image en noir et blanc
img = blackWhite(filter(blackWhite(img2gray(io.imread('horloge1.jpg'))), 3))

img1_FH = img.copy()
RogHeure1 = pc.rognageHeure(img1_FH)
img1_FH = pc.zoomIn(img1_FH,2,RogHeure1[0], RogHeure1[1], RogHeure1[2], RogHeure1[3])
img1_FHH = img1_FH.copy()

digit_heure = pc.decoupeChiffreHeure(img1_FHH)

heure_afficher = []
for i in digit_heure:
    heure_afficher.append( compareWithStandard(i, digitList) )

print(heure_afficher)