import cv2 as cv

#img = cv.imread("benedict.jpg")
#cv.imshow("Benedict", img)

#cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()