import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils
from imutils import contours


def detectNumbers(card, grayCard):
    # Temporal until we do the other parts
    card = cv2.imread("cardToDetect/carta1edge.png")
    card = cv2.cvtColor(card, cv2.COLOR_BGR2RGB)

    plt.imshow(card)
    plt.show()

    plt.imshow(card)
    plt.show()

    grayCard = cv2.cvtColor(card, cv2.COLOR_RGB2GRAY)
    grayCard = 255 - grayCard

    plt.imshow(grayCard, cmap="gray")
    plt.show()

    # Card numbers
    ref = cv2.imread("cardsTrain/numeroCartes2.png")
    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    plt.imshow(ref, cmap="gray")
    plt.show()
    ref = cv2.threshold(ref, 187, 255, cv2.THRESH_BINARY_INV)[1]

    plt.imshow(ref, cmap="gray")
    plt.show()

    # Contours of card numbers
    refCnts = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    refCnts = imutils.grab_contours(refCnts)
    refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]
    digits = {}

    refColor = cv2.cvtColor(ref, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(refColor, refCnts, -1, (0, 255, 0), 1)
    plt.imshow(refColor)

    # Cutting each number
    for (i, c) in enumerate(refCnts):
        # compute the bounding box for the digit, extract it, and resize
        # it to a fixed size
        (x, y, w, h) = cv2.boundingRect(c)
        roi = ref[y:y + h, x:x + w]
        # roi = cv2.resize(roi, (57, 88))
        # update the digits dictionary, mapping the digit name to the ROI
        digits[i] = roi
    # plt.imshow(digits[i], cmap="gray")
    # plt.show()

    # structuring kernel
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 9))
    sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # apply a tophat (whitehat) morphological operator to find light
    # regions against a dark background (i.e., the credit card numbers)
    tophat = cv2.morphologyEx(grayCard, cv2.MORPH_TOPHAT, rectKernel)
    plt.imshow(tophat, cmap="gray")
    plt.show()

    # compute the Scharr gradient of the tophat image, then scale
    # the rest back into the range [0, 255]
    gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
    gradX = gradX.astype("uint8")
    plt.imshow(gradX, cmap="gray")
    plt.show()

    # apply a closing operation using the rectangular kernel to help
    # cloes gaps in between credit card number digits, then apply
    # Otsu's thresholding method to binarize the image
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
    thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # apply a second closing operation to the binary image, again
    # to help close gaps between credit card number regions
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
    plt.imshow(thresh, cmap="gray")
    plt.show()
    cv2.imwrite("results/thresh.png", thresh)

    # find contours in the thresholded image, then initialize the
    # list of digit locations
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    locs = []

    # loop over the contours
    for (i, c) in enumerate(cnts):
        # compute the bounding box of the contour, then use the
        # bounding box coordinates to derive the aspect ratio
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        # find card size in pixels to discard the other shit
        if ar > 0.0 and ar < 3.5:
            # contours can further be pruned on minimum/maximum width
            # and height
            if (20 < w < 30) and (50 < h < 100):
                # append the bounding box region of the digits group
                # to our locations list
                locs.append((x, y, w, h))

    print(locs)

    output = []

    # loop over the 1 groupings of 1-2 digits
    for (i, (gX, gY, gW, gH)) in enumerate(locs):
        # initialize the list of group digits
        groupOutput = []
        # extract the group ROI of 4 digits from the grayscale image,
        # then apply thresholding to segment the digits from the
        # background of the credit card
        group = grayCard[gY - 5:gY + gH + 5, gX - 5:gX + gW + 5]
        group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # detect the contours of each individual digit in the group,
        # then sort the digit contours from left to right
        digitCnts = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        digitCnts = imutils.grab_contours(digitCnts)
        digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]

    conCard = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(conCard, digitCnts, -1, (255, 255, 0), 2)

    # loop over the digit contours
    for c in digitCnts:
        # compute the bounding box of the individual digit, extract
        # the digit, and resize it to have the same fixed size as
        # the reference OCR-A images
        (x, y, w, h) = cv2.boundingRect(c)
        roi = group[y:y + h, x:x + w]
        # roi = cv2.resize(roi, (57, 88))
        # initialize a list of template matching scores
        scores = []
        # loop over the reference digit name and digit ROI
        for (digit, digitROI) in digits.items():
            # apply correlation-based template matching, take the
            # score, and update the scores list
            result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCOEFF_NORMED)
            (_, score, _, _) = cv2.minMaxLoc(result)
            scores.append(score)
        # the classification for the digit ROI will be the reference
        # digit name with the *largest* template matching score
        print("[0,1,2,3,4,5,6,7,8,9]")
        print(scores)
        groupOutput.append(str(np.argmax(scores)))

        # draw the digit classifications around the group
        cv2.rectangle(card, (gX - 5, gY - 5), (gX + gW + 5, gY + gH + 5), (0, 0, 255), 2)
        cv2.putText(card, "".join(groupOutput), (gX, gY - 15), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        # update the output digits list
        output.extend(groupOutput)

    cv2.imshow("Image", card)
    cv2.waitKey(0)

    return groupOutput