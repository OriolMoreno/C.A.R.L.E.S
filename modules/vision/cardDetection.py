import cv2
import matplotlib.pyplot as plt
import numberDetection
import numpy as np
import imutils
from imutils import contours

CARD_MAX_AREA = 120000
CARD_MIN_AREA = 20000


def detectCards(image):
    # plt.imshow(image)
    # plt.show()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # plt.imshow(blur, cmap='gray')
    # plt.show()

    # Background distinction from cards
    img_w, img_h = np.shape(image)[:2]
    bkg_level = gray[int(img_h / 100)][int(img_w / 2)]
    thresh_level = bkg_level + 70

    _, thresh_image = cv2.threshold(blur, thresh_level, 255, cv2.THRESH_BINARY)

    plt.imshow(thresh_image)
    plt.show()

    cnts, parent = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    index_sort = sorted(range(len(cnts)), key=lambda i: cv2.contourArea(cnts[i]), reverse=True)

    if len(cnts) == 0:
        return []

    # Otherwise, initialize empty sorted contour and hierarchy lists
    cnts_sort = []
    hier_sort = []
    cnt_is_card = np.zeros(len(cnts), dtype=int)

    # Fill empty lists with sorted contour and sorted hierarchy. Now,
    # the indices of the contour list still correspond with those of
    # the hierarchy list. The hierarchy array can be used to check if
    # the contours have parents or not.
    for i in index_sort:
        cnts_sort.append(cnts[i])
        hier_sort.append(parent[0][i])

    # Determine which of the contours are cards by applying the
    # following criteria: 1) Smaller area than the maximum card size,
    # 2), bigger area than the minimum card size, 3) have no parents,
    # and 4) have four corners
    realCards = []
    cardCorners = []

    for i in range(len(cnts_sort)):
        size = cv2.contourArea(cnts_sort[i])
        peri = cv2.arcLength(cnts_sort[i], True)
        approx = cv2.approxPolyDP(cnts_sort[i], 0.01 * peri, True)

        if ((size < CARD_MAX_AREA) and (size > CARD_MIN_AREA)
                and (hier_sort[i][3] == -1) and (len(approx) == 4)):
            cnt_is_card[i] = 1
            realCards.append(cnts_sort[i])
            cardCorners.append(approx)
    return realCards, cardCorners


def extractCards(image, cardContours, cardCorners):
    cards = []
    i = 0
    for contour in cardContours:
        rect = np.zeros((4, 2), dtype="float32")

        rect[0] = cardCorners[i][1][0]  # top left
        rect[1] = cardCorners[i][0][0]  # top right
        rect[2] = cardCorners[i][3][0]  # bot right
        rect[3] = cardCorners[i][2][0]  # bot left

        # TODO: Check if cards are horizontal or vertical if vertical rotate
        w = rect[1] - rect[0]
        h = rect[2] - rect[3]

        print(w,h)

        x, y, w, h = cv2.boundingRect(contour)

        (tl, tr, br, bl) = rect

        maxWidth = 175

        maxHeight = 210
        # now that we have the dimensions of the new image, construct
        # the set of destination points to obtain a "birds eye view",
        # (i.e. top-down view) of the image, again specifying points
        # in the top-left, top-right, bottom-right, and bottom-left
        # order
        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")
        # compute the perspective transform matrix and then apply it
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
        #card = img[y:y + h, x:x + w]

        plt.imshow(warped)
        plt.show()

        i += 1
    return None
