import cv2
import matplotlib.pyplot as plt
import numberDetection
import cardDetection
import cardProcessing
import numpy as np
import imutils
from imutils import contours

img = cv2.imread("cardsTrain/cardBlackBackground.jpg")

img = cardProcessing.downscale(img)

cardContours = cardDetection.detectCards(img)

cardsFound = cardDetection.extractCards(img, cardContours)

#numberDetection.detectNumbers(card, grayCard)
