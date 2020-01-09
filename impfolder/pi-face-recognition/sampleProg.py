import numpy as np 
import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-n","--number",required=True,help="press num k")
args=vars(ap.parse_args())
img=cv2.imread('00000.png',0)
cv2.imshow('img',img)
if (args["number"])==27:
	cv2.destroyAllWindows()
elif (args["number"])==3:
	cv2.imwrite('viki.png',img)
	cv2.destroyAllWindows()
