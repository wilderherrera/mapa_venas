import sys
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import cv2
import numpy as np
from xlutils.copy import copy
from xlrd import open_workbook
import serial
import time
import xlwt
import os
global c,rb
rb = open_workbook('Registro.xls')
         
c=0
global num1,num2,num3,card,on,texto,check,ser,maxi,index

#ser=serial.Serial('COM9',9600,timeout=0.2)
texto=[]
texto.append('Wilder Herrera')
texto.append('Over Leon')

num1=cv2.imread('Logos/1.png')
num2=cv2.imread('Logos/2.png')
num3=cv2.imread('Logos/3.png')
card=cv2.imread('Logos/card.png')
reg=cv2.imread('Logos/reg.png')
check=cv2.imread('Logos/check.png')

num1=cv2.bitwise_not(num1)
num2=cv2.bitwise_not(num2)
num3=cv2.bitwise_not(num3)
on=0
maxi=False
resu=[]

#Precarga de administradores
imagenes=[]
imagenes.append(cv2.imread('Templates/Wilder Herrera.png',0))
imagenes.append(cv2.imread('Templates/Over_Leon.png',0))
#Interfaz de PubNub
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-6e938ef8-f0e6-4215-a092-824794c101e3'
pnconfig.subscribe_key = 'sub-c-53cabfec-3dd7-11e7-82b8-0619f8945a4f'
pubnub = PubNub(pnconfig) 
pubnub.subscribe().channels('my_channel').execute()

def publish_callback(result, status):
    pass
            
def hora():
    fecha=time.strftime("%d/%m/%y")
    hora=s=time.strftime("%H:%M:%S")
    total=hora+' '+fecha
    return(total)
    
def comp (img):
    suma=0
    [x,y]=img.shape
    x=range(x)
    y=range(y)
    for i in x:
        for j in y:
               if(img[i,j]==255):
                   suma=suma+1
    return(suma)

def todo(img):
    global maxi
    num1=img
    num1=num1[150:300, 200:450]

    num1=cv2.cvtColor(num1, cv2.COLOR_BGR2GRAY)

    num1=cv2.GaussianBlur(num1,(5,5),0)

    kernel = np.ones((10,10),np.float32)/100
    num1= cv2.filter2D(num1,-1,kernel)

    
    num1 = cv2.adaptiveThreshold(num1,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,23,1)


    
    num1=cv2.bitwise_not(num1)
    kernel = np.ones((2,2),np.uint8)
    num1=cv2.dilate(num1,kernel,iterations = 1)
    
    #FILTRADO FINAL
    num1=cv2.medianBlur(num1,13)
    #COMPARACION DE LA IMAGEN
    
    return(num1)

def conteo(num1):
    global maxi
    resut=[]
    resu=resut
    contador=len(imagenes)
    contador=range(contador)
    
    for i in contador:
        num2=cv2.bitwise_and(num1,imagenes[i])
        resul=comp(num2)
        
        if (resul>10000):
            maxi=1
        resu.append(resul)  
    busca=max(resu)
    ind=resu.index(busca)  
    return(ind)





def a():
    os.system('start excel C:\Users\herre\Desktop\Wilder_Unillanos\Semestre_IX\Bioingenieria_II\Proyecto\Registro.xls')
    
def registro1():
   

    global on,texto,check,index,ser,card,index
    
    target=0
    dato=raw_input("Ingrese Nuevo Nombre Para Registro:...")
    print(dato)
    #self.ventana.caja.setEnabled(True)
    texto.append(dato)
    #self.ventana.letras.setText('Ingrese Un Nombre...')
    if(len(texto)>0):
        index=len(texto)-1
        #self.ventana.letras.setText(texto[index])
        print texto[index]
        #self.ventana.letras.setText('Click en "Registrar Visitante"')
     
        index=len(texto)-1
        #self.ventana.caja.clear()
        #self.ventana.caja.setEnabled(False)
        #on=0
        global c,num3,num1,num2,card,rb
        timer=10
        suma=30
        ca=0
        c=0
        cap1=cv2.VideoCapture(1)
        while(True): 
##                        if(target!='1'):
##                             target=ser.read()    
##                             res=card
##                             print(target)
##                        elif(target=='1'):
                        _,im=cap1.read()
                        time.sleep(0.01)
                        c+=1
                        if(c<timer):
                                    res=reg
                                    
                        if(c>(timer)):
                                    res=im
                        if(c>(3*timer)and c<(timer*3.2)):
                                     toma=todo(res) 
                                     cv2.imwrite('Templates/'+texto[index]+'.png',toma)
                                     imagenes.append(cv2.imread('Templates/'+texto[index]+'.png',0))
                                     res=res*0;
                        if(c>timer*4 and c<timer*4.6):            
                            xx,yy,zz=im.shape
                            img2=cv2.resize(check,(yy,xx))
                            res=cv2.addWeighted(im,0.3,img2,0.7,0)
                        if(c>timer*5):            
                               ca=2
                    
                        cv2.imshow('Proceso',res)
                    
                    
                        if (cv2.waitKey(1) & 0xFF==ord('q'))or(ca==2):
                            cap1.release()
                            cv2.destroyAllWindows()
                            break                
            #self.ventana.letras.setText('Registro Completado')
        horas=hora()
        pubnub.publish().channel('canal1').message(['Nuevo Registro: '+texto[index],horas]).async(publish_callback)
        try:
            wb=copy(rb)
            ws=wb.get_sheet(0)
            style0 = xlwt.easyxf('font: name Arial, colour black, bold off')
            ws.write((index),4,"Nuevo Registro: ",style0)
            ws.write((index),5,texto[index],style0)
            ws.write((index),6,horas,style0)
            wb.save('Registro.xls')
        except:
            pubnub.publish().channel('canal1').message(['Cierre Hoja de calculo','Por Favor']).async(publish_callback)
            
        target='0'
        
def b():
    global c,num3,num1,num2,card,maxi
    c=0
    cap1=cv2.VideoCapture(1)
    timer=10
    suma=5
    ca=0
    while(ca==0):
        
                time.sleep(0.01)
                c+=1
                _,im=cap1.read()
                             
                #im=cv2.bitwise_not(im)
                toma=im[20:300, 100:600]
                toma=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  
                _,toma=cv2.threshold(toma,100,255,cv2.THRESH_BINARY)
                if(c<timer):
                    xx,yy,zz=im.shape
                    img2=cv2.resize(num3,(yy,xx))
                    res=cv2.addWeighted(im,0.3,img2,0.5,0)
                if(c>timer and c<timer+suma):
                    xx,yy,zz=im.shape
                    img2=cv2.resize(num2,(yy,xx))
                    res=cv2.addWeighted(im,0.3,img2,0.5,0)
                if(c>timer+suma and c<(2*timer+timer)):
                    xx,yy,zz=im.shape
                    img2=cv2.resize(num1,(yy,xx))
                    res=cv2.addWeighted(im,0.3,img2,0.5,0)
                    
                if (c>(2*timer+timer)):
                    res=im
                if(c>((5*timer+timer))and c<(5.8*timer+timer)):
                    cv2.imwrite('Nuevas\Foto.png',res)
                    res=res*0;
                if (c>((7*timer+timer))):
                        ca=2
       
                #res=cv2.bitwise_not(res)

                cv2.imshow('Proceso',res)

                
                if (cv2.waitKey(1) & 0xFF==ord('q'))or(ca==2):
                    cap1.release()
                    cv2.destroyAllWindows()
                    ca=1
    #res=cv2.imread('Nuevas/Foto.png')
    resulta=todo(res)
    resulta=conteo(resulta)
    ##########################
    horas=hora()
    if(maxi==1):
        print('Bienvenido '+texto[resulta])
        #self.ventana.letras.setText('Bienvenido '+texto[resulta])
        pubnub.publish().channel('canal1').message(['Bienvenido: '+texto[resulta],horas]).async(publish_callback)
    else:
        print('Acceso Denegado')
        #self.ventana.letras.setText('Acceso Denegado')
        pubnub.publish().channel('canal1').message(['Acceso Denegado',horas]).async(publish_callback)
    maxi=0
            
while(1): 
    my_listener = SubscribeListener()
    pubnub.add_listener(my_listener)
    pubnub.subscribe().channels('canal2').execute()
    my_listener.wait_for_connect()
    print('conectado')
    result = my_listener.wait_for_message_on('canal2').message[0]
    print result
    if(result=='a'):
        b()
    if(result=='r'):
        registro1()
    if(result=='m'):
        a()
        
 

    
    
