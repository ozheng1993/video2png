import numpy as np
import cv2
import math
import os
from sys import argv
import shutil
cap = cv2.VideoCapture(argv[1],0)
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
counter=0
counter2=0
a,b = str(argv[1]).split('.')
path = a
if len(argv)>2:
	fe=int(argv[2])
else:
	fe=200
if os.path.exists(a):
	shutil.rmtree(path)
os.mkdir(path)
f = open("./"+path+"/"+path+"Readme.txt", "w+")
f.write("test"+str(fe)) 
f.close() 
framePoint=fe

while(True):
	ret, frame = cap.read()
	framePoint = framePoint+fe
	cap.set(cv2.CAP_PROP_POS_FRAMES, framePoint)
	counter +=1
	if not ret:break
	# if (counter%fe!=0):
		
	# 	continue
	# else:
	counter2+=1
	cv2.imwrite("./"+path+"/"+path+"_"+str(counter2)+".png",frame)
	print("totoal: "+str(round(framePoint/frames*100,3))+"% || "+ "output image "+str(counter2)+ " / "+str(round(frames/fe,0))) 
	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
