import numpy as np
import cv2


num1=cv2.imread('Foto.png')
#cv2.imwrite('base.png',num1);
num1=num1[150:300, 200:450]

num1=cv2.cvtColor(num1, cv2.COLOR_BGR2GRAY)

num1=cv2.GaussianBlur(num1,(5,5),0)

kernel = np.ones((10,10),np.float32)/100
num1= cv2.filter2D(num1,-1,kernel)

num12=num1
num1 = cv2.adaptiveThreshold(num1,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,23,1)


num1=cv2.bitwise_not(num1)
kernel = np.ones((2,2),np.uint8)
num1=cv2.dilate(num1,kernel,iterations = 1)

#FILTRADO FINAL
num1=cv2.medianBlur(num1,13)
cv2.imshow('Proceso',num1)
cv2.imwrite('Williams Londoño.png',num1)
cv2.waitKey(0)
cv2.destroyAllWindows()

##cmpa=cv2.imread('wilder.png',0)
##
###COMPARACION DE LA IMAGEN
##num1=cv2.bitwise_and(num1,cmpa)
##resul=comp(num1)
##return(resul)

