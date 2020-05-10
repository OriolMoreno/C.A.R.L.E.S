import cv2
import numpy as np

def detectNumbers(card):

    grayCard = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    digits = {}

    for i in range(0, 12):
        dire = "train/numbers/" + str(i+1) + ".png"
        digits[i] = cv2.imread(dire, 0)

    groupOutput = []
    scores = []

    for (digit, digitROI) in digits.items():
        result = cv2.matchTemplate(np.uint8(grayCard), digitROI, cv2.TM_CCOEFF_NORMED)
        (_, score, _, _) = cv2.minMaxLoc(result)
        scores.append(score)

    print("[1,2,3,4,5,6,7,8,9,10,11,12]")
    print(scores)
    groupOutput.append(str(np.argmax(scores)+1))


    return groupOutput