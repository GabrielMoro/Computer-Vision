import cv2 as cv
import numpy as np

def floyd(img):
    img = img.astype('float32')
    row, col = img.shape
    for i in range(row):
        for j in range(col):
            old = img[i, j]
            new = (old > 128) * 255
            err = old - new
            img[i, j] = new
            if j + 1 < col:
                img[i, j + 1] += err * 7/16
            if i + 1 == row:
                continue
            if j > 0:
                img[i + 1, j - 1] += err * 3/16
            img[i + 1, j] += err * 5/16
            if j + 1 < col:
                img[i + 1, j + 1] += err * 1/16
    cv.imwrite('../out/halftoning/floyd.jpg', img)
    return img


def rogers(img):
    img = img.astype('float32')
    row, col = img.shape
    for i in range(row):
        for j in range(col):
            old = img[i, j]
            new = (old > 128) * 255
            err = old - new
            img[i, j] = new
            if j + 1 < col:
                img[i, j + 1] += err * 3/8
            if i + 1 == row:
                continue
            img[i + 1, j] += err * 3/8
            if j + 1 < col:
                img[i + 1, j + 1] += err * 2/8
    cv.imwrite('../out/halftoning/rogers.jpg', img)
    return img


def jarvis(img):
    img = img.astype('float32')
    row, col = img.shape
    for i in range(row):
        for j in range(col):
            old = img[i, j]
            new = (old > 128) * 255
            err = old - new
            img[i, j] = new
            if j + 1 < col:
                img[i, j + 1] += err * 7/48
                if j + 2 < col:
                    img[i, j + 2] += err * 5/48
            if i + 1 == row:
                continue
            if j - 1 > 0:
                img[i + 1, j - 1] += err * 5/48
                if j - 2 > 0:
                    img[i + 1, j - 2] += err * 3/48
            img[i + 1, j] += err * 7/48
            if j + 1 < col:
                img[i + 1, j + 1] += err * 5/48
                if j + 2 < col:
                    img[i + 1, j + 2] += err * 3/48
            if i + 2 == row:
                continue
            if j - 1 > 0:
                img[i + 2, j - 1] += err * 3/48
                if j - 2 > 0:
                    img[i + 2, j - 2] += err * 1/48
            img[i + 2, j] += err * 5/48
            if j + 1 < col:
                img[i + 2, j + 1] += err * 3/48
                if j + 2 < col:
                    img[i + 2, j + 2] += err * 1/48
    cv.imwrite('../out/halftoning/jarvis.jpg', img)
    return img


def stucki(img):
    img = img.astype('float32')
    row, col = img.shape
    for i in range(row):
        for j in range(col):
            old = img[i, j]
            new = (old > 128) * 255
            err = old - new
            img[i, j] = new
            if j + 1 < col:
                img[i, j + 1] += err * 8/42
                if j + 2 < col:
                    img[i, j + 2] += err * 4/42
            if i + 1 == row:
                continue
            if j - 1 > 0:
                img[i + 1, j - 1] += err * 4/42
                if j - 2 > 0:
                    img[i + 1, j - 2] += err * 2/42
            img[i + 1, j] += err * 8/42
            if j + 1 < col:
                img[i + 1, j + 1] += err * 4/42
                if j + 2 < col:
                    img[i + 1, j + 2] += err * 2/42
            if i + 2 == row:
                continue
            if j - 1 > 0:
                img[i + 2, j - 1] += err * 2/42
                if j - 2 > 0:
                    img[i + 2, j - 2] += err * 1/42
            img[i + 2, j] += err * 4/42
            if j + 1 < col:
                img[i + 2, j + 1] += err * 2/42
                if j + 2 < col:
                    img[i + 2, j + 2] += err * 1/42
    cv.imwrite('../out/halftoning/stucki.jpg', img)
    return img


img = cv.imread("../img/aqua.jpg")
cv.imshow("Original", img)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Floyd", floyd(img))
cv.imshow("Rogers", rogers(img))
cv.imshow("Jarvis", jarvis(img))
cv.imshow("Stucki", stucki(img))

cv.waitKey(0)
cv.destroyAllWindows()
