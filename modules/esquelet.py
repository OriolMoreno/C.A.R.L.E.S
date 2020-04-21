


#Variables globals
ActualPosition =  'NULL'

Cartama1=False
Cartama2=False
Cartama3=False


def ServoPositionsIniitial():


def ServoPositionsBaralla():


def ServoPositionsCartaRival():


def ServoPositionsCartaRobot():


def ServoPositionsCartama1():
    

def ServoPositionsCartama2():
   

def ServoPositionsCartama3():
       
    
def ServoPositionsGiradordeCarta():
    
    
    
def ServoPositionsRecollirCartaGirada():
    



def functionWifiConection():



def agafaCartaBaralla():
    #es mou a la baralla
    
    #podria enviar un missatge wifi demanat comprovació 
    #de camp visual lliure
    
    #agafa una carta de la baralla

    if Cartama1==False:
        #es mou a la posicio pertanyent a la cartaMa1
        ServoPositionsCartama1()
        Cartama1=True
        
    elif Cartama2==False:
        ServoPositionsCartama2()
        Cartama2=True
        
    elif Cartama3==False:
        ServoPositionsCartama3()
        Cartama3=True
    

def girarCarta():
    #Gira la carta portantla davant el girador, fent moviment ascendent
    # i deixant la caure
    #Després agafa la carta
    #La porta fins al taulell
    #La deixa caure al taulell

def tirarCartaBaralla():
    
    girarCarta();
    
    
    
def recollirCartes():
    #va a posicio carta adversari
    #l'agafa
    #porta la carta a la baralla de guanyades
    
    #va a posicio carta del robot
    #l'agafa
    #porta la carta a la baralla de guanyades
    
    agafaCartaBaralla()

def mouresAPosicioInicial():
    #fUNCIÓ POSA SERVOS A POSICIO INICAL ESTIGUI ON ESTIGUI
    
    
    #IDEA d'afegir una millora d'aquesta funció que es pugui moure un 
    #determinat temps, per anar fent el moviment i poder interrompel si
    #te una nova instrucció
    
    
    
    
def Move2InitialPositionIfNecessary():
    if ActualPosition!= InitialPoistion:
        mouresAPosicioInicial()



robotEnces=true
mouresAPosicioInicial()



while( robotEnces):
    
    while(readLecture=='False'):
        readLecture,positioMa= functionWifiConection()
        Move2InitialPositionIfNecessary()
    

    switch (readLecture):
        case 'agafaCartaBaralla':
            agafaCartaBaralla(positioMa)
            break;
            
        case 'tirarCarta':
            tirarCartaBaralla(positioMa)
            break;
            
                 
        case 'recollirCartes':
            recollirCartes()
            break;
        
        default:
            mouresAPosicioInicial()
            
            
        
