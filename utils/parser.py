import cv2
import os
import sys
from enum import Enum


import turicreate as tc
from turicreate import SFrame

class Parser(object):
	def __init__(self):
		pass

	@staticmethod
	def read_sframe(sframe_path):
		return tc.load_sframe(sframe_path).add_row_number()

	@staticmethod
	def parse_sframe(sframe, target=None, skip=5):
		assert (skip >= 1), "@Param 'skip' cannot be less than 1." 

		curr_frame = 0
		frames = {}
		boundings = {}

		while curr_frame < len(sframe['image']):
			frames[curr_frame] = sframe['image'][curr_frame].pixel_data
			boundings[curr_frame] = sframe['annotations'][curr_frame]

			# For writing the results of the bounding boxes.
			if target:
					cv2.imwrite(os.path.join(target, '{0}.jpg'.format(curr_frame)), frames[curr_frame])

			curr_frame += skip 

		return frames, boundings

	@staticmethod
	def delete_rows(sframe, ground_index, row_nums, target=None, name='new.sframe'):
		# Make new sframe
		sf = SFrame({'annotations': [sframe[ground_index]['annotations']], 'image': [sframe[ground_index]['image']]})

		for i in row_nums:
			sf = sf.append(SFrame({'annotations': [sframe[i]['annotations']], 'image': [sframe[i]['image']]}))

		if target:
			sf.save(name)

		return sf


