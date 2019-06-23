import utils.fingerprint as fp
import numpy as np
import cv2

from utils.parser import Parser
from utils.stats import select_logarithmic

from turicreate import SFrame

def select_distinct_frames(sframe_path, ground_index, skip=5, num_frames=10, factor=1.4, target=None):
	assert (factor > 1), "Factor has to be greater than 1."

	sf = Parser.read_sframe(sframe_path)
	frames, boundings = Parser.parse_sframe(sf, skip=skip)

	# Get ground frame.
	ground = frames[ground_index]
	ground_bounding = boundings[ground_index]

	# Initialize metrics and mapping lists for the similarity indices and mapping metrics to frame numbers.
	metrics = []
	mapping = {}

	for row_num, bounding in boundings.items():
		metric = fp.bounding_box_MSE(bounding, ground_bounding)
		metrics.append(metric)
		mapping[metric] = row_num

	metrics = sorted(metrics)
	selected = select_logarithmic(metrics, factor=factor)
	row_nums = []

	for metric in selected:
		row_num = mapping[metric]
		row_nums.append(row_num)

	new_sf = Parser.delete_rows(sf, ground_index, row_nums, target=target)
	return new_sf











	








