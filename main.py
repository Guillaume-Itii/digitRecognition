from math import pow

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

import pictCutter as pc

matplotlib.rcParams["font.size"] = 18


# Charge dans un tableau des chiffres préconstruit dans des TXT
def loadDigitTab():
    digit_list = []
    for i in range(0, 10):
        digit_list.append(np.loadtxt('./digitDB/' + str(i) + '.txt', delimiter=','))
        # print("-----Digit : " + str(i) + "-----")
        # print(digitList[i])
    return digit_list


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

def fullShow(a):
    fig, axes = plt.subplots(2, 4, figsize=(8, 4))
    ax = axes.ravel()
    for i in range(0,len(a)):
        ax[i].imshow(a[i])
    fig.tight_layout()
    plt.show()
# Compare l'image passé en paramètre avec la liste tiré de la base de donnée de chiffre
def compareWithStandard(digit_found, digitList,debug=False):
    min_error = 1
    number_mermory = 0
    number_mermory_list = []

    for i in range(0, len(digitList)):
        digit_created = resize(digit_found, digitList[i])[:, :, 0]

        error = np.mean(digit_found != digit_created)
        percent = (1 - error) * 100

        if error < min_error:
            min_error = error
            number_mermory = i
        if error <= min_error:
            number_mermory_list.append(i)

        if debug :
            print("Taux d'erreur pour " + str(i) + " : " + str(error))
            print("Taux de ressemblance pour " + str(i) + " : " + str(percent))
    if debug :
        print("Taux retenu : " + str(min_error))
        print("Chiffre potentiel : " + str(number_mermory))
        print("Autre chiffre possible : " + str(number_mermory_list))
        showBothPict(digit_found, digitList[number_mermory])
    return number_mermory


# Charge la liste de digit préconstruite
digitList = loadDigitTab()


img_enz = io.imread('horloge2.jpg')
img1_f_enz = img_enz.copy()
img1_f_enz = pc.filtreRouge(img1_f_enz)
img1_f_enz = pc.img2gray(img1_f_enz)
img1_f_enz = pc.NB(img1_f_enz)
img1_FH_enz = img1_f_enz.copy()
RogHeure1_enz = pc.rognageHeure(img1_FH_enz)
img1_FH_enz = pc.zoomIn(img1_FH_enz,2,RogHeure1_enz[0], RogHeure1_enz[1], RogHeure1_enz[2], RogHeure1_enz[3])
img1_FHH_enz = img1_FH_enz.copy()
digit_heure_enz = pc.decoupeChiffreHeure(img1_FHH_enz)

# Transforme une image en noir et blanc
img_kit = blackWhite(filter(blackWhite(img2gray(io.imread('horloge1.jpg'))), 3))
img1_FH_kit = img_kit.copy()
RogHeure1_kit = pc.rognageHeure(img1_FH_kit)
img1_FH_kit = pc.zoomIn(img1_FH_kit, 2, RogHeure1_kit[0], RogHeure1_kit[1], RogHeure1_kit[2], RogHeure1_kit[3])
img1_FHH_kit = img1_FH_kit.copy()
digit_heure_kit = pc.decoupeChiffreHeure(img1_FHH_kit)

fullShow(digit_heure_kit)
fullShow(digit_heure_enz)

heure_afficher = []
for i in digit_heure_kit:
    heure_afficher.append(compareWithStandard(i, digitList,True))

print(heure_afficher)

heure_afficher = []
for i in digit_heure_enz:
    heure_afficher.append(compareWithStandard(i, digitList,False))

print(heure_afficher)