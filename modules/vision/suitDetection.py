import cv2
import numpy as np


def findSuit(card):

    _, cardBinarized = cv2.threshold(cv2.cvtColor(card, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    dilation = cv2.dilate(cardBinarized, np.ones((1, 5)), iterations=2)
    opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, np.ones((1, 5)))

    cnts = cv2.findContours(opening, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cntsFiltered = []
    for cnt in cnts:
        # print(cv2.contourArea(cnt))
        if 1000 > cv2.contourArea(cnt) > 10:
            cntsFiltered.append(cnt)

    nlines = len(cntsFiltered)

    if nlines == 1:
        suit = "OROS"
    elif nlines == 2:
        suit = "COPAS"
    elif nlines == 3:
        suit = "ESPADAS"
    elif nlines == 4:
        suit = "BASTOS"
    else:
        suit = "ERROR"

    return suit
