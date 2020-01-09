import cv2
import numpy as np
import RPi.GPIO as GPIO

cap=cv2.VideoCapture(0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
while True:
	_,frame=cap.read()
	hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	low_red=np.array([161,155,84])
	high_red=np.array([179,255,255])
	mask=cv2.inRange(hsv_frame,low_red,high_red)
	nonzero=cv2.countNonZero(mask)
	if nonzero>500:
		print("varun")
		GPIO.setup(18,GPIO.OUT)
		GPIO.output(18,GPIO.HIGH)
	else: 
		GPIO.output(18,GPIO.LOW)
	cv2.imshow("mask",mask)
	key=cv2.waitKey(1) & 0xFF
	if key==27:
		break
