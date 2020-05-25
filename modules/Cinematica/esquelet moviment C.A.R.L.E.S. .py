
class CARLES:
     
    def __init__(self):
        #Variables globals
        self.ActualPosition =  'NULL'
        
        self.CartaOcupadaMa1=False
        self.CartaOcupadaMa2=False
        self.CartaOcupadaMa3=False
        
        #ANGLES
        self.Servo1=90
        self.Servo2=45
        self.Servo3=90
        self.Servo4=0


    def movimentServos(self):
        print("[moviment de braç realitzat]")
    
    
    def movimentVentosa(self):
        if self.Servo4==1:
            self.Servo4=0
            print("[Ventosa desactivada, carta deixada anar]")
        else:
            self.Servo4=1
            print("[Ventosa activada, carta agafada]")
    
    
    
    #Funcions de colocació d'angles + moviments
    def activarServosInicials(self):
        # ANGLES
        self.Servo1 = 90
        self.Servo2 = 45
        self.Servo3 = 90
        print("[angles definits]")
        self.movimentServos()
        print("ROBOT EN POSICIÓ BASE")
    
    
    
    
    def activarServosGiradordeCarta(self):
        # ANGLES
        self.Servo1 = 0
        self.Servo2 = 45
        self.Servo3 = 135
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = 0
        self.movimentVentosa()
    
        print("ROBOT A POSICIO GIRADOR DE CARTA AMB CARTA GIRANT-SE")
    
    
    def activarServosRecollirCartaGirada(self):
        #ANGLES
        self.Servo1 = 0
        self.Servo2 = 78.75
        self.Servo3 = 135
        self.movimentServos()
    
        self.Servo4 = 0
        self.movimentVentosa()
    
        print("ROBOT A POSICIO RECOLLIR CARTA RECENMENT GIRADA")
    
    
    def activarServosPilaDeCartesGuanyades(self):
        # ANGLES
        self.Servo1 = 40
        self.Servo2 = 67.5
        self.Servo3 = 90
        print("[angles definits]")
        self.movimentServos()

        self.movimentVentosa()
    
        print("ROBOT A POSICIO PILA DE CARTES GUANYADES AMB CARTA DESADA")
    
    
    def activarServosBaralla(self):
        #ANGLES
        self.Servo1 = 90
        self.Servo2 = 45
        self.Servo3 = 90
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = 0
        self.movimentVentosa()
    
        print("ROBOT A POSICIO BARALLA AMB CARTA AGAFADA")
    
    
    def activarServosTriumfo(self,bool_agafa_o_deixa=0):
        #ANGLES
        self.Servo1 = 90
        self.Servo2 = 45
        self.Servo3 = 135
        
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = bool_agafa_o_deixa
        self.movimentVentosa()

       
        if self.Servo4==1:  
            print("ROBOT A POSICIO TRIUMO AMB CARTA AGAFADA")
        else:
             print("ROBOT A POSICIO TRIUMO AMB CARTA TIRADA")
    
    
    def activarServosCartaRival(self):
        #ANGLES
        self.Servo1 = 65
        self.Servo2 = 67.5
        self.Servo3 = 90
        
        print("[angles definits]")
        self.movimentServos()
    
        self.movimentVentosa()
        
        print("ROBOT A POSICIO CARTA RIVAL AMB CARTA AGAFADA")
    
    
    def activarServosCartaRobot(self,bool_agafa_o_deixa=1):
        #ANGLES
        self.Servo1 = 120
        self.Servo2 = 67.5
        self.Servo3 = 90
        
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = bool_agafa_o_deixa
        self.movimentVentosa()
        
        if self.Servo4==1:  
            print("ROBOT A POSICIO CARTA C.A.R.L.E.S AMB CARTA AGAFADA")
        else:
            print("ROBOT A POSICIO CARTA C.A.R.L.E.S AMB CARTA DEIXADA")

    def activarServosCartama1(self,ventosa):
        # ANGLES
        self.Servo1 = 140
        self.Servo2 = 78.75
        self.Servo3 = 90
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = ventosa
        self.movimentVentosa()
        
        if self.Servo4==1:  
            print("ROBOT A POSICIO CARTA MA 1 AMB CARTA AGAFADA")
        else:
            print("ROBOT A POSICIO CARTA MA 1 AMB CARTA DEIXADA")
    
    def activarServosCartama2(self,ventosa):
        # ANGLES
        self.Servo1 = 160
        self.Servo2 =  78.75
        self.Servo3 = 90
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = ventosa
        self.movimentVentosa()
        
        if self.Servo4==1:  
            print("ROBOT A POSICIO CARTA MA 2 AMB CARTA AGAFADA")
        else:
            print("ROBOT A POSICIO CARTA MA 2 AMB CARTA DEIXADA")
    
    def activarServosCartama3(self,ventosa):
        # ANGLES
        self.Servo1 = 180
        self.Servo2 = 78.75
        self.Servo3 = 90
        print("[angles definits]")
        self.movimentServos()
    
        self.Servo4 = ventosa
        self.movimentVentosa()
        
        if self.Servo4==1:  
            print("ROBOT A POSICIO CARTA MA 3 AMB CARTA AGAFADA")
        else:
            print("ROBOT A POSICIO CARTA MA 3 AMB CARTA DEIXADA")
    
    
    # Funcions de conexió via wifi amb el programa
    
    
    #Funcions de moviments
    
    def agafaCartaBaralla(self):
        if (self.CartaOcupadaMa1==True and self.CartaOcupadaMa2==True and self.CartaOcupadaMa3==True):
            print("###############   ERROR:Totes les posicions de la ma estan ocupades   ###############")
            return 0
        while(self.CartaOcupadaMa1==False or self.CartaOcupadaMa2==False or self.CartaOcupadaMa3==False):
            #es mou a la baralla
            self.activarServosBaralla()
    
            #podria enviar un missatge wifi demanat comprovació
            #de camp visual lliure
    
            #agafa una carta de la baralla
            if self.CartaOcupadaMa1==False:
                #es mou a la posicio pertanyent a la cartaMa1
                self.activarServosCartama1(1)
                self.CartaOcupadaMa1=True
    
            elif self.CartaOcupadaMa2==False:
                self.activarServosCartama2(1)
                self.CartaOcupadaMa2=True
    
            elif self.CartaOcupadaMa3==False:
                self.activarServosCartama3(1)
                self.CartaOcupadaMa3=True
        return 1
        
        
    def agafaCartaMa(self,posicioMa):
       
        
            
        if posicioMa == 1:
            if self.CartaOcupadaMa1 == False:
                 print("###############   ERROR:No hi ha cap carta a la posició ",posicioMa, " de la ma  ###############")
                 return 0
            self.activarServosCartama1(0)
            self.CartaOcupadaMa1 = False
    
        elif posicioMa == 2:
            if self.CartaOcupadaMa2 == False:
                 print("###############   ERROR:No hi ha cap carta a la posició ",posicioMa, " de la ma  ###############")
                 return 0
            self.activarServosCartama2(0)
            self.CartaOcupadaMa2 = False
    
        elif posicioMa == 3:
            if self.CartaOcupadaMa3 == False:
                 print("###############   ERROR:No hi ha cap carta a la posició ",posicioMa, " de la ma  ###############")
                 return 0
            self.activarServosCartama3(0)
            self.CartaOcupadaMa3 = False
        
        return 1
    
    def tirarCarta(self):
        #Gira la carta portantla davant el girador, fent moviment ascendent
        # i deixant la caure
        self.activarServosGiradordeCarta()
    
        # Després agafa la carta
        self.activarServosRecollirCartaGirada
    
    
        #La porta fins al taulell
        self.activarServosCartaRobot()
    
    
    
    def tirarCartaMa(self, posicioMa):
    
        if  (self.CartaOcupadaMa1==False and self.CartaOcupadaMa2==False and self.CartaOcupadaMa3==False):
            print("###############   ERROR:Totes les posicions de la ma estan buides   ###############")
            return 0
        
        if  0==self.agafaCartaMa(posicioMa):
            return 0
        
        
        self.tirarCarta();
        return 1
    
    
        
        
    def recollirCartes(self):
        self.activarServosCartaRival()
        
        self.activarServosPilaDeCartesGuanyades()
        
        self.activarServosCartaRobot(0)
        
        self.activarServosPilaDeCartesGuanyades()
        
        self.agafaCartaBaralla()
    
    def mouresAPosicioInicial(self):
        #fUNCIÓ POSA SERVOS A POSICIO INICAL ESTIGUI ON ESTIGUI
        self.activarServosInicials()
        
        #IDEA d'afegir una millora d'aquesta funció que es pugui moure un 
        #determinat temps, per anar fent el moviment i poder interrompel si
        #te una nova instrucció
        
        
    def tirarTriumfo(self):
        self.activarServosBaralla()
        
        self.activarServosTriumfo()
        
    def recollirTriumfo(self):
        self.activarServosTriumfo()
        
        self.activarServosPilaDeCartesGuanyades()
        
        
        
    def Move2InitialPositionIfNecessary(self):
        #Aquest funció era amb la idea de moure el braç a la posicio inicial del braç sempre
        # que no tingues ninguna acció en curs o en espera. Aquesta funcionalitat tindria en compte que si
        # es demana una nova acció, aturaria el moviment a la posició base
        #i iniciaria el nou moviment
        #if ActualPosition!= InitialPoistion:
        #    mouresAPosicioInicial()

        hola='NO'




#main del programa

carles=CARLES()
print("------------------------------------")
print("------INCICIALITZANT C.A.R.L.E.S ------")
robotEnces=True
carles.mouresAPosicioInicial()
comanda=1###ADD
posicioMa=2###ADD
print("---------C.A.R.L.E.S PREPARAT---------------")

while( robotEnces):
    #comanda, readLecture,posicioMa= functionWifiConection()
    test=['tirarTriumfo', 'agafaCartaBaralla','tirarCarta', 'recollirCartes', 'agafaCartaBaralla', 'tirarCarta', 'recollirTriumfo']
    for readLecture in test:
        if comanda==1:
            if readLecture=='agafaCartaBaralla' :
                print("------------------------------------")
                print("------INCICIANT ACCIÓ AGAFAR CARTA/S BARALLA ------")
                if carles.agafaCartaBaralla():
                    print("------CARTA/S EN MA ------")
                    print("------------------------------------") 
               
                

            elif readLecture == 'tirarCarta':
                print("------------------------------------")
                print("------INCICIANT ACCIÓ TIRAR CARTA MA ",posicioMa," ------")
                if carles.tirarCartaMa(posicioMa):
                    print("------CARTA DE LA MA NUMERO ", posicioMa, " TIRADA ------")
                    print("------------------------------------") 
                else:
                    print("------S'HA DONAT UN ERROR ------")
                    print("------------------------------------") 
                
            elif readLecture == 'recollirCartes':
                print("------------------------------------")
                print("------INCICIANT ACCIÓ RECOLLIR CARTES ------")
                carles.recollirCartes()
                print("------CARTES A LA PILA DE GUANYADES I NOVA CARTA EN MA ------")
                print("------------------------------------") 
                

            elif readLecture == 'recollirTriumfo':
                print("------------------------------------")
                print("------INCICIANT RECOLLIR TRIUMFO ------")
                carles.recollirTriumfo()
                print("------CARTA TRIUMFO RECOLLLIDA ------")
                print("------------------------------------") 
                
                

            elif readLecture == 'tirarTriumfo':
                print("------------------------------------")
                print("------INCICIANT ACCIÓ TIRAR TRIUMFO ------")
                carles.tirarTriumfo()
                print("------TRIUMFO RECOLLIT ------")
                print("------------------------------------")

            else:
                carles.mouresAPosicioInicial()
     
    robotEnces=0
        
def programaPrincipal():
    return 0, 'Nothing', 1;



def functionWifiConection():
    #Funció que reb una comanda que ordena una acció del robot C.A.R.L.E.S.
    comanda, readLecture,posicioMa= programaPrincipal();

    return  comanda, readLecture,posicioMa;



