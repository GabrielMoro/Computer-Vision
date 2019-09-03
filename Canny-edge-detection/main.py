import cv2 as cv

def canny(img, sigma):

    img = cv.GaussianBlur(img,(3,3),sigma)

    sobel_x = cv.convertScaleAbs(cv.Sobel(img,cv.CV_32F,1,0,ksize=3))
    sobel_y = cv.convertScaleAbs(cv.Sobel(img,cv.CV_32F,0,1,ksize=3))

    res = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    return res


sigma = 0
img = cv.imread('../img/keanu.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

m_canny = canny(img, sigma)

cv.imshow('Manual', m_canny)
cv.imshow('OpenCV', cv.Canny(img, 100, 150))

cv.imwrite('../out/manual_canny.jpg', m_canny)

cv.waitKey(0)
cv.destroyAllWindows()
