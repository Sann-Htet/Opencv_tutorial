import cv2 as cv
import numpy as np

img = cv.imread('benedict.jpg')
cv.imshow('Benedict', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 - 90), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Maksed", masked)

cv.waitKey(0)