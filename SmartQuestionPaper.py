import numpy as np
import cv2

img = cv2.imread('Python/contours.png')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

for cnt in contours:
    M = cv2.moments(cnt)
    area = cv2.contourArea(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print('Centroid =',cx, cy, '\tArea = ', area) 



cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()