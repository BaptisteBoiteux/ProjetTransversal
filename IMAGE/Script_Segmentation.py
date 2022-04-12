import cv2
import matplotlib.pyplot as plt
import numpy as np

##----------------------------------------------------------------------------##
##-----------------Initialisation de la base de référence---------------------##
##----------------------------------------------------------------------------##

ImRef = []
#ImRef.append(cv2.imread("img_test_2_1T_ref.png"))
#ImRef.append(cv2.imread("TEST_REF.png"))
ImRef.append(cv2.imread('TEST11_REF.jpg'))
#ImRef.append(cv2.imread("IMAGE_TEST_CAMERA_REF.jpg"))

gray_ImRef = []
for i in range (0, len(ImRef)):  # transformation en niveau de gris
    gray_ImRef.append(cv2.cvtColor(ImRef[i], cv2.COLOR_BGR2GRAY))
    
th_ImRef = []
for i in range (0, len(ImRef)):  # seuillage
    th = cv2.threshold(gray_ImRef[i],5,255,cv2.THRESH_BINARY)[1]
    th_ImRef.append(th)
    
contours_ImRef = []  
for i in range (0, len(ImRef)):  # extraction des contours
    contours = cv2.findContours(th_ImRef[i],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
    contours_ImRef.append(contours)
    
airs_ImRef = []
#airs2_ImRef = []
for i in range (0, len(ImRef)):  # extraction des caractéristiques
    airs_ImRef.append(cv2.contourArea(contours_ImRef[i][0]))
    #x,y,w,h = cv2.boundingRect(contours_ImRef[i][0])
    #airs2_ImRef.append(w*h)


##----------------------------------------------------------------------------##
##------------------------Segmentation par seuillage--------------------------##
##----------------------------------------------------------------------------##
    
def ref_nb(x):
    return {
        0: 0,
        1: 1,
        2: 2,
        3: 3
    }.get(x,1)

def photo(image):
    cam = cv2.VideoCapture(1)
    res, Image = cam.read()
    if res:
        #cv2.imshow(image,Image)
        cv2.imwrite(image,Image)

def seuillage_otsu(image):
    im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    s = cv2.split(im_hsv)[1]
    th_s = cv2.threshold(s,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    #cv2.imwrite("th_s.png",th_s)
    return th_s

def Lissage(image,th_s):
    th = th_s

    #Ajouts de bord à l'image
    bordersize=10
    th = cv2.copyMakeBorder(th, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )

    #Remplissage des contours
    im_floodfill = th.copy()
    h, w = th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (0,0), 255)
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    th = th | im_floodfill_inv
    
    #Enlèvement des bord de l'image
    th = th[bordersize: len(th)-bordersize,bordersize: len(th[0])-bordersize]
    resultat = cv2.bitwise_and(image,image,mask=th)
    #cv2.imwrite("im_floodfill.png",im_floodfill)
    #cv2.imwrite("th.png",th)
    #cv2.imwrite("resultat.png",resultat)
    return th

def Objets(image,th):
    contours = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
    Objs=[]
    for i in range (0, len(contours)) :
        mask_Obj_i = np.zeros((len(th),len(th[0])), np.uint8)
        x,y,w,h = cv2.boundingRect(contours[i])
        cv2.drawContours(mask_Obj_i, contours, i, (255,255,255), -1)
        Obj_i = cv2.bitwise_and(image,image,mask=mask_Obj_i)
        if h >15 and w>15 :
            Obj_i = Obj_i[y:y+h,x:x+w]
            Objs.append(Obj_i);
            #cv2.imwrite("BB_"+str(i)+".png",BB_i)
    return Objs

def Area(Objs):
    gray_Objs = []
    for i in range (0, len(Objs)):  # transformation en niveau de gris
        gray_Objs.append(cv2.cvtColor(Objs[i], cv2.COLOR_BGR2GRAY))
    th_Objs = []
    for i in range (0, len(Objs)):  # seuillage
        th = cv2.threshold(gray_Objs[i],5,255,cv2.THRESH_BINARY)[1]
        th_Objs.append(th)
    contours_Objs = []  # extraction des contours
    for i in range (0, len(Objs)):
        contours = cv2.findContours(th_Objs[i],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
        contours_Objs.append(contours)
        
    airs_Objs = []
    #airs2_Objs = []
    #airs3_Objs = []
    for i in range (0, len(Objs)):  # extraction des caractéristiques
        airs_Objs.append(cv2.contourArea(contours_Objs[i][0]))
        x,y,w,h = cv2.boundingRect(contours_Objs[i][0])
        #airs2_Objs.append(w*h)
        #airs3_Objs.append(x*y)
        
    return airs_Objs 

def Area_max(airs):
    air_max = 0
    i_max = 0
    for i in range(0, len(airs)):
        if airs[i] > air_max:
            air_max = airs[i]
            i_max = i
    return air_max, i_max

def Comparaison(air_max,air_ref):
    verif = False
    if abs(air_max-air_ref) < (1/10)*air_ref:
        verif = True
    return  verif


##----------------------------------------------------------------------------##
##----------------------Algorithme de Détection-------------------------------##
##----------------------------------------------------------------------------##

def Detection(ref,image):
    
    #photo(image)

    im = cv2.imread(image)
    imref_nb = ref_nb(ref)

    th_s = seuillage_otsu(im)
    th = Lissage(im,th_s)
    Objs = Objets(im,th)

    airs_Objs = Area(Objs)

    air_max = Area_max(airs_Objs)[0]
    i_max = Area_max(airs_Objs)[1]

    verif = Comparaison(air_max,airs_ImRef[imref_nb])
    if verif:
        cv2.imwrite('RESULT.png',Objs[i_max])
    
    print(verif,imref_nb)
    print(air_max)
    print(airs_ImRef[imref_nb])

Detection(0,'TEST11.jpg')