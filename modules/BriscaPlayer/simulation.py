import random
from briscaPlayer import partida

def GenerarBaralla():
    baralla = []
    pals = ['b', 'e', 'o', 'c']
    for pal in pals:
        for i in range(1, 4):
            baralla.append((i, pal))
    return baralla

def iniciarPartida(baralla):
    p = partida()
    # Robot agafa primera carta de la pila, la gira i la posa a l'slot de la pinta
    p.pinta = baralla.pop()
    # Robot agafa les 3 següents cartes de la pila i les posa a la seva ma
    for i in range(3):
        p.ma.append(baralla.pop())
    return p

def pintarTaulellObert(p, maH,cartesTaula,baralla): #anar ampliant
    print("Ma de la IA: ", p.ma)
    print("Pinta: ", p.pinta)
    print("Cartes sobre la Taula: ", cartesTaula)
    print("Nombre de cartes a la pila:", len(baralla))
    print("Ma del jugador: ", maH)
    print(" ")

def humaRoba(baralla,maH): # simulació de que l'humà roba una carta
    maH.append(baralla.pop())

def IARoba(baralla,p):
    p.ma.append(baralla.pop())

def robotJugaCarta(p,indexCarta, cartesTaula): # simulació de que el robot tira una carta
    cartesTaula.append(p.ma.pop(indexCarta))

def nomCarta(carta):
    if carta[1] == 'b': pal = "bastos"
    elif carta[1] == 'o': pal = "oros"
    elif carta[1] == 'e': pal = "espases"
    else: pal = "copes"

    return str(carta[0])+" de "+pal

def humaJugaCarta(p,cartesTaula,maH): # simulació de que l'humà tira una carta
    if cartesTaula:
        print("En C.A.R.L.E.S ha jugat un ", nomCarta(cartesTaula[0]))
        print(" ")
        #pintarTaulellObert(p,maH,cartesTaula)

    print("A la teva ma tens les següents cartes: ",maH)
    print("Quina vols jugar? (1, 2 o 3)")
    indexCarta = input()
    print(" ")
    while indexCarta not in ['1','2','3']:
        print("Si us plau, introdueix una carta vàlida (1, 2 o 3)")
        indexCarta = input()

    cartesTaula.append(maH.pop(int(indexCarta)-1))

def IArecullCartesGuanyades(cartesGuanyadesIA,cartesTaula,p):
    for i in range(2):
        p.puntsIA += p.valorNumeros[cartesTaula[0][0]]
        cartesGuanyadesIA.append(cartesTaula.pop(0))

def HrecullCartesGuanyades(cartesGuanyadesH,cartesTaula,p):
    for i in range(2): #,carta in enumerate(cartesTaula):
        p.puntsH += p.valorNumeros[cartesTaula[0][0]]
        cartesGuanyadesH.append(cartesTaula.pop(0))

def simulacioPartidaObert():
    baralla = GenerarBaralla()
    random.shuffle(baralla)
    p = iniciarPartida(baralla)

    ### Dir a l'humà que roba tres cartes ###

    # humà roba tres cartes
    maHuma = []
    for i in range(3):
        humaRoba(baralla,maHuma)

    cartesSobreLaTaula = []
    cartesGuanyadesIA = []
    cartesGuanyadesH = []

    pintarTaulellObert(p,maHuma,cartesSobreLaTaula,baralla)

    # comença sempre tirant primer la IA, per simplificar
    ### Fer que digui quelcom gracioset ###
    comencaH = False

    while len(baralla) > 0:
        if not comencaH: # Comença tirant la IA
            cartaATirar = p.TriarCarta(False)
            # El robot juga la carta escollida
            robotJugaCarta(p,cartaATirar,cartesSobreLaTaula)
            # Torn de l'humà
            # pintarTaulellObert(p, maHuma, cartesSobreLaTaula)
            # L'humà juga una carta
            humaJugaCarta(p,cartesSobreLaTaula,maHuma)
            #pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

            if p.guanyaIA(cartesSobreLaTaula[0],cartesSobreLaTaula[1],False): #cartaIA, cartaH, comencaH
                print("Aquesta ronda la guanya en C.A.R.L.E.S.! \n")
                # El robot mou les cartes guanyades a l'slot corresponent
                IArecullCartesGuanyades(cartesGuanyadesIA,cartesSobreLaTaula,p)

                # El robot roba una carta de la pila
                print("En C.A.R.L.E.S. roba una carta")
                IARoba(baralla,p)
                print("Robes una carta\n")
                if len(baralla) > 0: humaRoba(baralla,maHuma)
                pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)
            else:
                print("Guanyes aquesta ronda!\n")
                # L'humà recull de la taula les cartes guanyades
                HrecullCartesGuanyades(cartesGuanyadesH, cartesSobreLaTaula, p)

                print("Robes una carta")
                humaRoba(baralla, maHuma)
                print("En C.A.R.L.E.S. roba una carta\n")
                if len(baralla) > 0: IARoba(baralla, p)
                pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)
                comencaH = True
        else: # comença l'humà
            # L'humà juga una carta
            humaJugaCarta(p, cartesSobreLaTaula, maHuma)
            pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

            cartaATirar = p.TriarCarta(True,cartesSobreLaTaula[0])
            # El robot juga la carta escollida
            robotJugaCarta(p, cartaATirar, cartesSobreLaTaula)
            print("En C.A.R.L.E.S. juga un ", nomCarta(cartesSobreLaTaula[1]))
            #pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

            if p.guanyaIA(cartesSobreLaTaula[1],cartesSobreLaTaula[0],True): #cartaIA, cartaH, comencaH
                print("Aquesta ronda la guanya en C.A.R.L.E.S.! \n")
                # El robot mou les cartes guanyades a l'slot corresponent
                IArecullCartesGuanyades(cartesGuanyadesIA,cartesSobreLaTaula,p)

                # El robot roba una carta de la pila
                print("En C.A.R.L.E.S. roba una carta")
                IARoba(baralla,p)
                print("Robes una carta\n")
                if len(baralla) > 0: humaRoba(baralla,maHuma)
                pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)
                comencaH = False
            else:
                print("Guanyes aquesta ronda!\n")
                # L'humà recull de la taula les cartes guanyades
                HrecullCartesGuanyades(cartesGuanyadesH, cartesSobreLaTaula, p)

                print("Robes una carta")
                humaRoba(baralla, maHuma)
                print("En C.A.R.L.E.S. roba una carta\n")
                if len(baralla) > 0: IARoba(baralla, p)
                pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

    if len(maHuma) == 2:
        # L'humà robarà la pinta si és la única carta que queda
        maHuma.append(p.pinta[:])
    elif len(p.ma) == 2:
        # El robot faria el mateix
        ### Funcio perquè el robot ho faci
        p.ma.append(p.pinta[:])
    else:
        print("No m'agraden les trampes")
        return





    # Últimes 3 cartes. A la millora, minmax
    for i in range(3):
        if not comencaH: # Comença tirant la IA
            cartaATirar = p.TriarCarta(False)
            # El robot juga la carta escollida
            robotJugaCarta(p,cartaATirar,cartesSobreLaTaula)
            # L'humà juga una carta
            humaJugaCarta(p,cartesSobreLaTaula,maHuma)
            pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

            if p.guanyaIA(cartesSobreLaTaula[0],cartesSobreLaTaula[1],False): #cartaIA, cartaH, comencaH
                print("Aquesta ronda la guanya en C.A.R.L.E.S.! \n")
                # El robot mou les cartes guanyades a l'slot corresponent
                IArecullCartesGuanyades(cartesGuanyadesIA,cartesSobreLaTaula,p)
            else:
                print("Guanyes aquesta ronda!\n")
                # L'humà recull de la taula les cartes guanyades
                HrecullCartesGuanyades(cartesGuanyadesH, cartesSobreLaTaula, p)
                comencaH = True
        else: # comença l'humà
            # L'humà juga una carta
            humaJugaCarta(p, cartesSobreLaTaula, maHuma)
            pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

            cartaATirar = p.TriarCarta(True,cartesSobreLaTaula[0])
            # El robot juga la carta escollida
            robotJugaCarta(p, cartaATirar, cartesSobreLaTaula)
            print("En C.A.R.L.E.S. juga un ", nomCarta(cartesSobreLaTaula[1]))
            pintarTaulellObert(p, maHuma, cartesSobreLaTaula,baralla)

            if p.guanyaIA(cartesSobreLaTaula[1],cartesSobreLaTaula[0],True): #cartaIA, cartaH, comencaH
                print("Aquesta ronda la guanya en C.A.R.L.E.S.! \n")
                # El robot mou les cartes guanyades a l'slot corresponent
                IArecullCartesGuanyades(cartesGuanyadesIA,cartesSobreLaTaula,p)
                comencaH = False
            else:
                print("Guanyes aquesta ronda!\n")
                # L'humà recull de la taula les cartes guanyades
                HrecullCartesGuanyades(cartesGuanyadesH, cartesSobreLaTaula, p)


    # Final de la partida:
    print("No cal que comptis les cartes, ja ho he fet jo")
    print("Tu has aconseguit",p.puntsH,"punts,")
    print("I en C.A.R.L.E.S. ,", p.puntsIA, ".")
    print("Per tant...")
    if p.puntsH > p.puntsIA:
        print("Has guanyat, enhorabona!")
    else:
        print("Ha guanyat en C.A.R.L.E.S.")
        print("Sempre pots tornar-ho a intentar: Ell no es cansarà mai, li encanta la brisca!")
    print(cartesGuanyadesIA)
    print(cartesGuanyadesH)

if __name__ == '__main__':
    simulacioPartidaObert()
