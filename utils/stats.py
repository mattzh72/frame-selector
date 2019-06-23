import numpy as np
import bisect

class Stats(object):
	@staticmethod
	def generate_cutoffs(n, lst):
		scale = 0
		p = scale * 100 / (n - 1)

		cutoffs = []
		while p <= 100:
			cutoffs.append(np.percentile(lst, p))
			scale += 1
			p = scale * 100 / (n - 1)

		return cutoffs

	@staticmethod
	def slice_off_percentile(lst, threshhold):
		# Cut away lower threshold.
		cutoff = np.percentile(lst, threshhold)
		lst = lst[bisect.bisect_right(lst, cutoff):]

		return lst

	@staticmethod
	def select_percentile(n, lst):
		cutoffs = Stats.generate_cutoffs(n + 1, lst)
		selected = []

		for i in range(0, len(cutoffs) - 1):
			start = bisect.bisect_left(lst, cutoffs[i])
			end = bisect.bisect_right(lst, cutoffs[i+1])

			print(start, end)

			selected.append(lst[start + (end - start) // 2])

		return selected

	@staticmethod
	def select_uniform(n, lst, threshhold=25):
		if threshhold: 
			lst = Stats.slice_off_percentile(lst, threshhold)

		factor = len(lst) // n
		selected = [lst[i] for i in range(len(lst)) if i % factor == 0]

		return selected

	@staticmethod
	def select_logarithmic(lst, factor=1.4):
		dist = len(lst)
		selected = []
		while dist:
			dist = dist // factor
			selected.append(lst[len(lst) - int(dist) - 1])

		return selected



