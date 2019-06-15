import cv2
import os
import sys

def parse(video, target=None, write=False, skip=5): 
	vid = cv2.VideoCapture(video)
	ret,frame = vid.read()

	currFrame = 0
	frames = {}

	while(ret):
		if currFrame % skip == 0:
			frames[currFrame] = frame

			if target and write:
				cv2.imwrite(os.path.join(target, '{0}.jpg'.format(currFrame)), frame)

		currFrame += 1
		ret,frame = vid.read()

	vid.release()
	cv2.destroyAllWindows()

	return frames
