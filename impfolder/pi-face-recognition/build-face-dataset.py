#USAGE
#python build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/vikas
#import necessary package
from imutils.video import VideoStream
import argparse
import imutils
import time
import os
import cv2
#constructing the argument parser
path="/home/pi/pi-face-recognition"
ap=argparse.ArgumentParser()
ap.add_argument("-c","--cascade",required=True,help="path to where the face cascade resides")
ap.add_argument("-o","--output",required=True,help="path to output directory")
args=vars(ap.parse_args())

detector=cv2.CascadeClassifier(args["cascade"])

print("[INFO] starting video Stream...")
vs=VideoStream(src=0).start()
#vs=VideoStream(usePiCamera=True).start()
time.sleep(2.0)
total=0
while True:
	frame=vs.read()
	orig=frame.copy()
	frame=imutils.resize(frame,width=400)
	rects=detector.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
	for (x,y,w,h) in rects:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow("Frame",frame)
	key=cv2.waitKey(1) & 0xFF
	if key == ord("k"):
		p=os.path.sep.join([args["output"],"{}.png".format(str(total).zfill(5))])
		cv2.imwrite(p,orig)
		total+=1
	elif key==ord("q"):
		break
print("[INFO] {} face images stored".format(total))
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()