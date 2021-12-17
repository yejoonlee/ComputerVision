import sys
import cv2

# output
cap1 = cv2.VideoCapture('./practice_output/1.chroma_key.avi')

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(0)

    if key == 27:
        break

cap1.release()
cv2.destroyAllWindows()