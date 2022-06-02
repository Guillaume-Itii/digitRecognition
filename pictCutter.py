from skimage import io
import numpy as np

img1 = io.imread('horloge1.jpg')
img2 = io.imread('horloge2.jpg')

# detection taille image
longueur1 = np.size(img1,1)
largeur1 = np.size(img1,0)
print("longueur img 1 : ", longueur1, ", largeur img2 : ", largeur1)

longueur2 = np.size(img2,1)
largeur2 = np.size(img2,0)
print("longueur img 2 : ", longueur2, ", largeur img2 : ", largeur2)

def filtreRouge(img):
    longueur = np.size(img, 1)
    largeur = np.size(img, 0)
    for i in range(longueur):
        for j in range(largeur):
            if img[j, i, 0] > 220:
                img[j, i, 0] =img[j, i, 1] = img[j, i, 2] = 255
            else:
                img[j, i, 0] = img[j, i, 1] = img[j, i, 2] = 0
    return(img)

def rognage(img):
    longueur = np.size(img, 1)
    largeur = np.size(img, 0)
    coin1_x = coin1_y = coin2_x = coin2_y = 0
    for i in range(longueur):
        for j in range(largeur):
            if img[j, i] == 255:
                if (coin1_x or coin1_y) == 0:
                    if coin1_x == 0:
                        coin1_x = i
                    if coin1_y == 0:
                        coin1_y = j
                else:
                    if j > coin2_y:
                        coin2_y = j
                    if i > coin2_x:
                        coin2_x = i
                    if i < coin1_x:
                        coin1_x = i
                    if j < coin1_y:
                        coin1_y = j
    return(coin1_x, coin1_y, coin2_x, coin2_y)

def rognageHeure(img):
    coin1_x = coin1_y = coin2_x = coin2_y = 0
    longueur = np.size(img, 1)
    largeur = np.size(img, 0)
    for i in range(500):
        for j in range(largeur):
            if img[j, i] == 255:
                if (coin1_x or coin1_y) == 0:
                    if coin1_x == 0:
                        coin1_x = i
                    if coin1_y == 0:
                        coin1_y = j
                else:
                    if j > coin2_y:
                        coin2_y = j
                    if i > coin2_x:
                        coin2_x = i
                    if i < coin1_x:
                        coin1_x = i
                    if j < coin1_y:
                        coin1_y = j
    return (coin1_x, coin1_y, coin2_x, coin2_y)

def rognageReste(img):
    coin1_x = coin1_y = coin2_x = coin2_y = 0
    longueur = np.size(img, 1)
    largeur = np.size(img, 0)
    for i in range(500, longueur,1):
        for j in range(largeur):
            if img[j, i] == 255:
                if (coin1_x or coin1_y) == 0:
                    if coin1_x == 0:
                        coin1_x = i
                    if coin1_y == 0:
                        coin1_y = j
                else:
                    if j > coin2_y:
                        coin2_y = j
                    if i > coin2_x:
                        coin2_x = i
                    if i < coin1_x:
                        coin1_x = i
                    if j < coin1_y:
                        coin1_y = j
    return (coin1_x, coin1_y, coin2_x, coin2_y)


def zoomIn(image, zoom, x1, y1, x2, y2):
    if zoom < 2: zoom = 2
    if zoom > 10: zoom = 10
    image = image[y1:y2, x1:x2]
    if len(image.shape) == 2:
        return np.kron(image, np.ones((zoom, zoom)))
    else:
        return np.kron(image, np.ones((zoom, zoom, 1))).astype(np.uint8)

def decoupeChiffreHeure(img):
    longueur = np.size(img, 1)
    largeur = np.size(img, 0)
    l_c = longueur / 4
    l_c = int(l_c)

    C1 = img.copy()
    C1 = zoomIn(C1, 2, 1, 1, l_c, largeur)
    C1_r = rognage(C1)
    C1 = zoomIn(C1, 2, C1_r[0], C1_r[1], C1_r[2], C1_r[3])
    io.imshow(C1)
    io.show()

    C2 = img.copy()
    C2 = zoomIn(C2, 2, l_c, 1, (2*l_c), largeur)
    C2_r = rognage(C2)
    C2 = zoomIn(C2, 2, C2_r[0], C2_r[1], C2_r[2], C2_r[3])
    io.imshow(C2)
    io.show()

    C3 = img.copy()
    C3 = zoomIn(C3, 2, 2*l_c, 1, 3*l_c, largeur)
    C3_r = rognage(C3)
    C3 = zoomIn(C3, 2, C3_r[0], C3_r[1], C3_r[2], C3_r[3])
    io.imshow(C3)
    io.show()

    C4 = img.copy()
    C4 = zoomIn(C4, 2, 3*l_c, 1, longueur, largeur)
    C4_r = rognage(C4)
    C4 = zoomIn(C4, 2, C4_r[0], C4_r[1], C4_r[2], C4_r[3])
    io.imshow(C4)
    io.show()

def decoupeChiffreReste(img):
    longueur = np.size(img, 1)
    largeur = np.size(img, 0)
    l_c = (longueur / 3)*1.05
    l_c = int(l_c)

    C1 = img.copy()
    C1 = zoomIn(C1, 2, 1, 1, l_c, int(largeur/2))
    C1_r = rognage(C1)
    C1 = zoomIn(C1, 2, C1_r[0], C1_r[1], C1_r[2], C1_r[3])
    io.imshow(C1)
    io.show()

    C2 = img.copy()
    C2 = zoomIn(C2, 2, l_c, 1, (2*l_c), int(largeur/2))
    C2_r = rognage(C2)
    C2 = zoomIn(C2, 2, C2_r[0], C2_r[1], C2_r[2], C2_r[3])
    io.imshow(C2)
    io.show()

    C3 = img.copy()
    C3 = zoomIn(C3, 2, 1, int(largeur/2), l_c, largeur)
    C3_r = rognage(C3)
    C3 = zoomIn(C3, 2, C3_r[0], C3_r[1], C3_r[2], C3_r[3])
    io.imshow(C3)
    io.show()

    C4 = img.copy()
    C4 = zoomIn(C4, 2, l_c, int(largeur/2), 2*l_c, largeur)
    C4_r = rognage(C4)
    C4 = zoomIn(C4, 2, C4_r[0], C4_r[1], C4_r[2], C4_r[3])
    io.imshow(C4)
    io.show()

def img2gray(img1) :
    grey=np.dot(img1,[0.2125,0.7154,0.0721])
    return grey

def NB (img) :
    img[img>=89] = 255
    img[img<=89] = 0
    return img

# Image de base
#io.imshow(img1)
#io.show()
#io.imshow(img2)
#io.show()



#Image filtré rouge
img1_f = img1.copy()
img1_f = filtreRouge(img1_f)
img1_f = img2gray(img1_f)
#io.imshow(img1_f, cmap = "gray")
#io.show()
img1_f = NB(img1_f)
#io.imshow(img1_f)
#io.show()


img2_f = img2.copy()
img2_f = filtreRouge(img2_f)
img2_f = img2gray(img2_f)
#io.imshow(img2_f)
#io.show()
img2_f = NB(img2_f)
#io.imshow(img2_f)
#io.show()


#Test rognage heure#########################################################################################
img1_FH = img1_f.copy()
RogHeure1 = rognageHeure(img1_FH)
img1_FH = zoomIn(img1_FH,2,RogHeure1[0], RogHeure1[1], RogHeure1[2], RogHeure1[3])
#io.imshow(img1_FH)
#io.show()

img2_FH = img2_f.copy()
RogHeure2 = rognageHeure(img2_FH)
img2_FH = zoomIn(img2_FH,2,RogHeure2[0], RogHeure2[1], RogHeure2[2], RogHeure2[3])
#io.imshow(img2_FH)
#io.show()

#Detection chiffres heure
img1_FHH = img1_FH.copy()
decoupeChiffreHeure(img1_FHH)

img2_FHH = img2_FH.copy()
decoupeChiffreHeure(img2_FHH)

#Test rognage reste
img1_RR = img1_f.copy()
RogReste1 = rognageReste(img1_RR)
print(RogReste1)
img1_RR = zoomIn(img1_RR,2,RogReste1[0], RogReste1[1], RogReste1[2], RogReste1[3])
io.imshow(img1_RR)
io.show()

img2_RR = img2_f.copy()
RogReste2 = rognageReste(img2_RR)
print(RogReste2)
img2_RR = zoomIn(img2_RR,2,RogReste2[0], RogReste2[1], RogReste2[2], RogReste2[3])
#io.imshow(img2_RR)
#io.show()

#Detection chiffres reste
img1_RRR = img1_RR.copy()
decoupeChiffreReste(img1_RRR)

img2_RRR = img2_RR.copy()
decoupeChiffreReste(img2_RRR)
