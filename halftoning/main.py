from half import *

img = cv.imread("../img/aqua.jpg")
cv.imshow("Original", img)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Floyd", floyd(img))
cv.imshow("Rogers", rogers(img))
cv.imshow("Jarvis", jarvis(img))
cv.imshow("Stucki", stucki(img))

cv.waitKey(0)
cv.destroyAllWindows()
