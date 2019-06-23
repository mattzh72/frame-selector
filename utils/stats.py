import numpy as np
import bisect

def segment_uniform(n, lst):
	scale = 0
	p = scale * len(lst) / n

	result = []
	while p < len(lst):
		start = int(p)
		scale += 1
		p = scale * len(lst) / n
		end = int(p)

		result.append(lst[start:end])

	return result

def segment_by_percentile(n, lst):
	cutoffs = generate_cutoffs(n, lst)
	result = []

	for i in range(0, len(cutoffs) - 1):
		start = bisect.bisect_left(lst, cutoffs[i])
		end = bisect.bisect_right(lst, cutoffs[i+1])

		result.append(lst[start:end])

	return result

def generate_cutoffs(n, lst):
	scale = 0
	p = scale * 100 / (n - 1)

	cutoffs = []
	while p <= 100:
		cutoffs.append(np.percentile(lst, p))
		scale += 1
		p = scale * 100 / (n - 1)

	return cutoffs

def slice_off_percentile(lst, threshhold):
	# Cut away lower threshold.
	cutoff = np.percentile(lst, threshhold)
	lst = lst[bisect.bisect_right(lst, cutoff):]

	return lst

def select_uniform(n, lst, threshhold=25):
	if threshhold: 
		lst = slice_off_percentile(lst, threshhold)

	factor = len(lst) // n
	selected = [lst[i] for i in range(len(lst)) if i % factor == 0]

	return selected

def select_logarithmic(lst, factor=1.4):
	dist = len(lst)
	selected = []
	while dist:
		dist = dist // factor
		selected.append(lst[len(lst) - int(dist) - 1])

	return selected



