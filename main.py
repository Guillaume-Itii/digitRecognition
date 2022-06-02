from skimage import io
import numpy as np
from math import pow
import matplotlib.pyplot as plt
import matplotlib
from io import StringIO

matplotlib.rcParams["font.size"] = 18


def loadDigitTab():
    digitList = []
    for i in range(0, 10):
        digitList.append(np.loadtxt('./digitDB/' + str(i) + '.txt', delimiter=','))
        # print("-----Digit : " + str(i) + "-----")
        # print(digitList[i])
    return digitList


def imgToTxt(img, file):
    destination = open(file + ".txt", "w")
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


def resize(digit_found, digit_created):
    C = digit_created

    w, h = C.shape[:2];

    xNew = np.shape(digit_found)[0];
    yNew = np.shape(digit_found)[1];

    xScale = xNew / (w - 1);
    yScale = yNew / (h - 1);

    newImage = np.zeros([xNew, yNew, 1]);

    for i in range(xNew - 1):
        for j in range(yNew - 1):
            newImage[i + 1, j + 1] = C[1 + int(i / xScale),
                                       1 + int(j / yScale)]
    return newImage


def showBothPict(a,b):
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()
    ax[0].imshow(a)
    ax[1].imshow(b)
    fig.tight_layout()
    plt.show()

def compareWithStandard(digit_found, digitList):
    for i in range(0, len(digitList)):
        digit_created = resize(digit_found,digitList[i])[:, :, 0]
        print(digit_created)

        error = np.mean(digit_found != digit_created)
        percent = (1-error)*100

        print("Taux d'erreur pour "+ str(i) +" : " + str(error) )
        print("Taux de ressemblance pour "+ str(i) +" : " + str(percent) )

        showBothPict(digit_found,digit_created)



digitList = loadDigitTab()

img = blackWhite(filter(blackWhite(img2gray(io.imread('horloge1.jpg'))), 3))

digit_found = getDigit(img)

compareWithStandard(digit_found, digitList)