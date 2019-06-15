import numpy as np
import cv2
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt

def avg(lst): 
    return sum(lst) / len(lst) 

# Load images
ground = cv2.imread("./data/ground.jpg", 0)
near = cv2.imread("./data/near.jpg", 0)
far = cv2.imread("./data/far.jpg", 0)

orb = cv2.ORB_create()
kpg, desg = orb.detectAndCompute(ground, None)
kpn, desn = orb.detectAndCompute(near, None)
kpf, desf = orb.detectAndCompute(far, None)

show = np.hstack([
		cv2.drawKeypoints(ground, kpg, None, color=(0,255,0), flags=0),
		cv2.drawKeypoints(near, kpn, None, color=(0,255,0), flags=0),
		cv2.drawKeypoints(far, kpf, None, color=(0,255,0), flags=0)
	])
plt.imshow(show)
plt.show()

# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches_near = bf.knnMatch(desg,desn, k=1)
# matches_far = bf.knnMatch(desg,desf, k=1)

# dist_near = np.array([m[0].distance for m in matches_near if m])
# dist_far = np.array([m[0].distance for m in matches_far if m])

# print((np.square(dist_near)).mean())
# print((np.square(dist_far)).mean())