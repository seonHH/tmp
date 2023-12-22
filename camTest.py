import sys
import cv2

print('getting cam view')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('load cam fail')

while True:
    _, frame  = cap.read()
    cv2.imshow('test', frame)
    key = cv2.waitKey(50)
    if key == 'q':
        break