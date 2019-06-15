import utils.fingerprint as fp
import numpy as np
import os
import cv2
import random
import pickle

from utils.parser import parse
from utils.stats import segment_by_percentile, select_by_percentile
from config import Configs

# Get every fifth frame.
if Configs.PARSE:
	frames = parse('vid.mov', target=Configs.TARGET_DIR, write=Configs.WRITE, skip=Configs.SKIP)

	# Get ground frame.
	ground = frames[Configs.GROUND_INDEX]

	# Initialize distinct frames lst and map.
	metrics = []
	mapping = {}

	# Initialize orb.
	orb = cv2.ORB_create()

	for name, frame in frames.items():
		metric = fp.correlate(frame, ground)
		metrics.append(metric)
		mapping[metric] = name

	# Cache metrics.
	with open(os.path.join(Configs.PICKLE_DIR, 'correlate.pickle'), 'wb') as handle:
		pickle.dump({
				'metrics': metrics,
				'mapping': mapping,
				'frames': frames,
				'ground': ground
			}, handle, protocol=pickle.HIGHEST_PROTOCOL)

else:
	with open(os.path.join(Configs.PICKLE_DIR, 'correlate.pickle'), 'rb') as handle:
		data = pickle.load(handle)
		metrics, mapping, frames, ground = sorted(data['metrics']), data['mapping'], data['frames'], data['ground']

		selected = select_by_percentile(Configs.NUM_FRAMES, metrics, threshhold=20)
		for metric in selected:
			name = mapping[metric]
			frame = frames[name]

			cv2.imwrite(os.path.join(Configs.TARGET_DIR, '{0}.jpg'.format(name)), frame)







	








