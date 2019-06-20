import cv2
import os
import sys
from enum import Enum


import turicreate
from turicreate import SFrame

class Parser(object):
	def __init__(self):
		pass

	@staticmethod
	def read_sframe(sframe, target=None, skip=5):
		assert (skip >= 1), "@Param 'skip' cannot be less than 1." 

		sf = turicreate.load_sframe(sframe)
		curr_frame = 0
		frames = {}

		while curr_frame < len(sf['image']):
			frames[curr_frame] = sf['image'][curr_frame].pixel_data

			if target:
					cv2.imwrite(os.path.join(target, '{0}.jpg'.format(curr_frame)), frames[curr_frame])

			curr_frame += skip 

		return frames

	@staticmethod
	def read_video(video, target=None, skip=5): 
		assert (skip >= 1), "@Param 'skip' cannot be less than 1."

		vid = cv2.VideoCapture(video)
		ret,frame = vid.read()

		curr_frame = 0
		frames = {}

		while(ret):
			if curr_frame % skip == 0:
				frames[curr_frame] = frame

				if target:
					cv2.imwrite(os.path.join(target, '{0}.jpg'.format(curr_frame)), frame)

			curr_frame += 1
			ret,frame = vid.read()

		vid.release()
		cv2.destroyAllWindows()

		return frames


