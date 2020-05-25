# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:31:54 2020

@author: Victor
"""


import numpy as np
import math
L0=2
L1=18
L2=16
L3=1

squL0=L0**2
squL1=L1**2
squL2=L2**2

#Coordenades inicials de la base del robot
glob_x_inicial=0
glob_Y_inicial=0
glob_Z_inicial=0

angulo1=0
angulo2=0
angulo0rads=0

x,y,z=0,0,0

contador=0

rangeAngulo0=range(0,180)

rangeAngulo1=range(45,90)

rangeAngulo2=range(45,135)

def calculAnglePerZ(y,x):
    
    theta=angulo0rads=math.atan2(y,x)
    
    angulo0EnGrados=angulo0rads*180 / math.pi
    
    return angulo0EnGrados
    


def calculAnglesPerXY(x,y):

    
    angulo2=abs(math.acos(((x**2)+(y**2)+(z**2)-(L1**2)-(L2**2))/(2*L1*L2)))
    angulo2EnGrados= angulo2*180 / math.pi

    
    angulo1=abs((math.atan2(y,abs(math.sqrt((x**2)+(y**2))))*180 / math.pi)-(math.atan2(L2*(math.sin(angulo2)*180 / math.pi),L1+L2*(math.cos(angulo2)*180 / math.pi)))*180 / math.pi)
    angulo1EnGrados=angulo1
    
    
    


    return angulo1EnGrados,angulo2EnGrados



def calculsDelsAngles(text,x,y,z,contador):
    
    
    angulo0=calculAnglePerZ(y,x)
    
    
    
    angulo1, angulo2= calculAnglesPerXY(x,y)

    
    contador=visualitzation(text,angulo0, angulo1, angulo2,x,y,z,contador,pointview1=45,pointview2=45)
    
    return contador






def visualitzation (text,angulo0, angulo1, angulo2,x,y,z,contador,pointview1,pointview2):
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    
    
   
    
   
    
    #Calcul de coords finals part 1 braç
    part1_fi_z=abs(math.cos(math.radians(abs(90-angulo1))))*L1
    
    
    co=abs(math.cos(math.radians(angulo1))*L1)
    
    
    
    y2=math.cos(math.radians(abs(90-angulo0)))*co
    x2=math.cos(math.radians(angulo0))*co
    
    
    part1_fi_x=x2
    part1_fi_y=y2
     
    
    
    part2_inici_x=part1_fi_x
    
    part2_inici_y=part1_fi_y
        
    
    part2_fi_x=x
    
    part2_fi_y=y
    
    
    part2_fi_x=x
    
    part2_fi_y=y
    
        
    fig = plt.figure()
    ax = fig.add_subplot( projection='3d',fc='w')    
    fig.suptitle(text, fontsize=16)
    
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    ax.set_xlim( [-30, 30]  )
    ax.set_ylim( [0, 30]  )
    ax.set_zlim( [0, 30]  )
    
    ax.view_init(0, 0)
    fig.tight_layout()
    
    VecStart_x = [0,part2_inici_x,x]
    VecStart_y = [0,part2_inici_y,y]
    VecStart_z = [0,part1_fi_z,z]
    VecEnd_x =  [part1_fi_x,x,x]
    VecEnd_y =  [part1_fi_y,y,y-0.1]
    VecEnd_z  = [part1_fi_z,z,z]
    
    
    for i in range(3):
        ax.plot(xs=[VecStart_x[i], VecEnd_x[i]], ys=[VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])
    
    ax.view_init(pointview1,pointview2)
    plt.savefig('Traslació/plt'+str(contador)+'.png')
    plt.show()
    
    contador=contador+1
    return contador



def trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador):
    
    '''
    ################################################# EXPLICCIÓ ######################################################
    Com que transportem un pes molt lleuger, no ens cal tenir en conte esforços maxims (transportem cartes)
    
    #Com que es un robot ideat per relacionar-se amb persones de la tercera edat no volem que es mogui a una velocitat rapida
    
    La trajectoria rectelinia continua es la mes idonea ja que es la mes clara vist des de la perspectiva humana
    
    #Per aixo fariem servi la llibreria de Llibreria VarSpeedServo.h de Arduino
    #################################################################################################################
    '''
    
    x_medias=[]
    if x_new<x:
        x_medias=np.arange(x_new, x, 1).tolist()
        x_medias.reverse()
    else:
        x_medias=np.arange(x, x_new, 1).tolist()
        
        
    y_medias=[]
    if y_new<y:
        y_medias=np.arange(y_new, y, 1).tolist()
        y_medias.reverse()
    else:
        y_medias=np.arange(y, y_new, 1).tolist()
        
        
    z_medias=[]    
    if z_new<z:
        z_medias=np.arange(z_new, z, 1).tolist()
        z_medias.reverse()
    else:
        z_medias=np.arange(z, z_new, 1).tolist() 
    
    #xm ym son Punto medio entre dos puntos

    lenMaxim=max(len(x_medias),len(y_medias),len(z_medias))
    
    for t in range(lenMaxim-1):
        if t<len(x_medias):
            x_traslacio=x_medias[t]
        else:
            x_traslacio=x_new
            
        if t<len(y_medias):
            y_traslacio=y_medias[t]
        else:
            y_traslacio=y_new
        
        if t<len(z_medias):
            z_traslacio=z_medias[t]
        else:
            z_traslacio=z_new
        
        
        contador=calculsDelsAngles(text,x_traslacio,y_traslacio,z_traslacio,contador)
    
    return calculsDelsAngles(text,x_new,y_new,z_new,contador)
    
'''
MAIN PROGRAM
'''

'''
MAIN PROGRAM
'''

print("BENVINGUT AL PROGRAMA:")
print(" ")
print(" ")

print("Aquest es el braç antropomofic de'n C.A.R.L.E.S")
print(" ")    
print("Inicialment esta en aquesta posició:")

x=15
y=15
z=4
text="C.A.R.L.E.S TRANSLATION SIMULATION"

contador=calculsDelsAngles(text,x,y,z,contador)
    
print("Vols seleccionar uns punts de l'espai per veure com s'hi mou el C.A.R.L.E.S.? (y/n/exit)")
resposta=input('Input:')


if(resposta=='y'or resposta=='Y'):
    
    print("A quins punts vol moure el braç del robot de l'espai de treball?")
    
    print("Quina x nova vol selecionar?")
    x_new=float(input('Input:'))
    print("La x nova seleccionada es:", x_new)
 
    print("Quina y nova vol selecionar?")
    y_new=float(input('Input:'))
    print("La y nova seleccionada es:", y_new)
    
    print("Quina z nova vol selecionar?")
    z_new=float(input('Input:'))
    print("La z nova seleccionada es:", z_new)
    
    print("A continuacíó es calcularan eles geometricament i veures una visulaitzaciuó aproximada--------->")
    text="C.A.R.L.E.S a posicions seleccionades pel client--------->"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
elif (resposta!="exit"):
    print("Aquí tens una mostra random:")
    print("Es el moviment que fa per agafar una carta i girarla--------->") 


    print("Agafa la carta de la ma")
    x_new=25
    y_new=15
    z_new=10
    text="C.A.R.L.E.S agafa la carta de la ma"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    print("Es mou a la posició inici per no fer moviments poc intuitus per l'humà")
    x_new=15
    y_new=15
    z_new=4
    text="C.A.R.L.E.S es mou a posició inici amb carta agafada"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    print("Es mou a la posició on esta el mecanisme girador de cartes")
    x_new=-20
    y_new=15
    z_new=4
        
    text="C.A.R.L.E.S es mou a girador de cartes"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    x_new=-20
    y_new=1
    z_new=4
    text="C.A.R.L.E.S es mou a girador de cartes"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    print("Ara aixeca la carta per girarla")
    x_new=-20
    y_new=1
    z_new=9
    text="C.A.R.L.E.S aixeca la carta per girarla"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    print("Ara recull la carta girada")
    x_new=-32
    y_new=1
    z_new=1
    text="C.A.R.L.E.S recull la carta girada"   
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    x_new=-32
    y_new=1
    z_new=4
    text="C.A.R.L.E.S recull la carta girada"   
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    
    print("Finalment porta la carta girada al taulell")
    x_new=12
    y_new=20
    z_new=4
    text="C.A.R.L.E.S porta la carta girada al taulell"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    x_new=12
    y_new=20
    z_new=0
    text="C.A.R.L.E.S porta la carta girada al taulell"
    contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
    x=x_new
    y=y_new
    z=z_new
    
    print("finale celebration:")
    for q in range (3):
        x_new=-4
        y_new=10
        z_new=7
        
        text="C.A.R.L.E.S està content i celebra"
        contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
        x=x_new
        y=y_new
        z=z_new
        
        x_new=4
        y_new=10
        z_new=7
            
        contador=trajectoriaRectiliniaContínua(text,x_new,y_new,z_new,contador)
        x=x_new
        y=y_new
        z=z_new
