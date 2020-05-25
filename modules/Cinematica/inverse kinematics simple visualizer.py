# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:31:54 2020

@author: Victor
"""

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

x,y,z=0,0,0


rangeAngulo0=range(0,180)

rangeAngulo1=range(45,90)

rangeAngulo2=range(45,135)

def calculAnglePerZ(z,x):
    
    theta=angulo0rads=math.atan2(z,x)
    
    angulo0EnGrados=angulo0rads*180 / math.pi
    
    print("Angulo0: ",angulo0EnGrados)
    return angulo0EnGrados
    


def calculAnglesPerXY(longitudx,y):

    #y=y-L0
    
    h=math.sqrt((longitudx**2)+(y**2))
    squ_h=h**2
    
    alpha=math.atan2(y,longitudx)*180 / math.pi
    
    beta=math.acos(  (squL1-squL2+squ_h)/(2*L1*h)   )*180 / math.pi
    
    
    angulo1EnGrados=abs(alpha-beta)
    
    angulo2EnGrados= abs((math.acos((squL1+squL2-squ_h)/(2*L1*L2) )*180 / math.pi )- 180)
    
    
    
    print("Angulo1: ",angulo1EnGrados)

    print("Angulo2: ",angulo2EnGrados)

    return angulo1EnGrados,angulo2EnGrados



def calculsDelsAngles():
    
    
    angulo0=calculAnglePerZ(z,x)
    
    
    longitudx=math.sqrt((x**2)+(z**2))
    
    angulo1, angulo2= calculAnglesPerXY(longitudx,y)

    visualitzation(angulo0, angulo1, angulo2,pointview1=0,pointview2=0)
    
    visualitzation(angulo0, angulo1, angulo2,pointview1=45,pointview2=60)
    
    return angulo0, angulo1, angulo2






def visualitzation (angulo0, angulo1, angulo2,pointview1,pointview2):
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    #Calcul de coords finals part 1 braç
    adjj=math.cos(math.radians(angulo1))*L1
    part1_fi_x=adjj+glob_x_inicial
    print("part 1 - x coord final: ", part1_fi_x)
    
    opp=math.sin(math.radians(angulo1))*L1
    part1_fi_y=opp+glob_Y_inicial
    print("part 1 - y coord final: ", part1_fi_y)

    #Calcul de la z:
    hz=adjj*math.cos(math.radians(angulo0-90))

    part1_fi_z=hz*math.cos(math.radians(angulo0))
    
     
    
    
    
    #Calcul de coords inicials  part 2 braç:
    part2_inici_x=part1_fi_x
    print("part 2 - x coord inicial: ", part2_inici_x)
    
    part2_inici_y=part1_fi_y
    print("part 2 - y coord inicial: ", part2_inici_y)
        
    
    #Calcul de coords inicials part 2 braç
    part2_fi_x=x
    print("part 2 - x coord final: ", part2_fi_x)
    
    part2_fi_y=y
    print("part 2 - y coord final: ", part2_fi_y)
    
    
    #Calcul de coords de z del braç
    part2_fi_x=x
    print("part 2 - x coord final: ", part2_fi_x)
    
    part2_fi_y=y
    print("part 2 - y coord final: ", part2_fi_y)
    
        
    fig = plt.figure()
    ax = fig.add_subplot( projection='3d',fc='w')    
    
    plt.title('Simulació posició final braç',fontsize=16, color='k')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Z Label')
    ax.set_zlabel('Y Label')
    ax.view_init(0, 0)
    fig.tight_layout()
    
    VecStart_x = [glob_x_inicial,part2_inici_x,part2_fi_x]
    VecStart_y = [glob_Y_inicial+2,part2_inici_y,part2_fi_y]
    VecStart_z = [0,part1_fi_z,z]
    VecEnd_x =  [part1_fi_x,part2_fi_x,part2_fi_x]
    VecEnd_y =  [part1_fi_y,part2_fi_y,part2_fi_y-0.1]
    VecEnd_z  = [part1_fi_z,z,z]
    
    
    #error
    tamanySilumacioL1=L1
    tamanySilumacioL1=math.sqrt(((part1_fi_x-glob_x_inicial)**2)+((part1_fi_y-glob_Y_inicial)**2))
    
    if L1 != tamanySilumacioL1:
        print("ERROR L1 malament: Robot no pot arribar a tal posició")
        
        
    tamanySilumacioL2=L2
    tamanySilumacioL2=math.sqrt(((part2_fi_x-part2_inici_x)**2)+((part2_fi_y-part2_inici_y)**2))
    #if L2 != tamanySilumacioL2:
        #print("ERROR L2 malament: Robot no pot arribar a tal posició")
        
        
    for i in range(3):
        ax.plot([VecStart_x[i], VecEnd_x[i]], zs=[VecStart_y[i],VecEnd_y[i]],ys=[VecStart_z[i],VecEnd_z[i]])
    
    ax.view_init(pointview1,pointview2)
    
'''
MAIN PROGRAM
'''

print("Benvingut al programa:")
    
print("Vols seleccionar uns punts de l'espai per veure com s'hi mou el C.A.R.L.E.S.? (y/n)")
resposta=input('Input:')
    


if(resposta=='y'):
    
    print("A quins punts vol moure el braç del robot de l'espai de treball?")
    
    print("Quina x vol selecionar?")
    x=float(input('Input:'))
    print("La x seleccionada es:", x)
 
    print("Quina y vol selecionar?")
    y=float(input('Input:'))
    print("La y seleccionada es:", y)
    
    print("Quina z vol selecionar?")
    z=float(input('Input:'))
    print("La z seleccionada es:", z)
    
    print("A continuacíó es calcularan eles geometricament i veures una visulaitzaciuó aproximada--------->")

else:
    print("Aquí tens una mostra random--------->")
    x=20
    z=12
    y=4
    
angulo0, angulo1, angulo2=calculsDelsAngles()

