import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
	_,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	edged=cv2.Canny(gray,30,200)
	cv2.imshow('canny image',edged)
	cv2.imshow('gray image',gray)
	key=cv2.waitKey(1) & 0xFF
	if key==27:
		break
