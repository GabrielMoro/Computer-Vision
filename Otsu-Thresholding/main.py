import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def otsu(img):
    hist = cv.calcHist([img],[0],None,[256],[0,256])

    sumTotal = 0
    for i in range(256):
        sumTotal += i * hist[i][0]

    totalPx = img.size
    maxVar = 0
    wb = 0
    wf = 0
    sumB = 0

    for i in range(256):
        wb += hist[i][0]
        wf = totalPx - wb
        if(wb == 0 or wf == 0):
            continue
        
        sumB += i * hist[i][0]
        meanB = sumB / wb
        meanF = (sumTotal - sumB) / wf

        var = wb * wf * (meanB - meanF)**2
        if(var > maxVar):
            maxVar = var
            trshold = i

    print(f'Threshold: {trshold}')

    row, col = img.shape
    for i in range(row):
        for j in range(col):
            if img[i, j] > trshold:
                img[i, j] = 255
            else:
                img[i, j] = 0

    return img


img = cv.imread("img/img1.jpg")
cv.imshow("Original", img)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_,opencvOtsu = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("OpenCV Otsu", opencvOtsu)

manualOtsu = otsu(img)
cv.imwrite("img/manual_otsu.jpg", manualOtsu)
cv.imshow("Manual Otsu", manualOtsu)

cv.waitKey(0)
cv.destroyAllWindows()
