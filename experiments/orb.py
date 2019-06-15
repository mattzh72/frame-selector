import numpy as np
import cv2
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt

# Load images
ground = cv2.imread("./data/ground.jpg", 0)
near = cv2.imread("./data/close_far.jpg", 0)
far = cv2.imread("./data/far.jpg", 0)

orb = cv2.ORB_create(edgeThreshold=15, patchSize=31, nlevels=8, fastThreshold=20, scaleFactor=1.2, WTA_K=2,scoreType=cv2.ORB_HARRIS_SCORE, firstLevel=0, nfeatures=10)
kpg, kpn, kpf = orb.detect(ground), orb.detect(near), orb.detect(far)
pts_g = np.array([kpg[i].pt for i in range(0, len(kpg))]).astype(np.float32)
pts_n = np.array([kpn[i].pt for i in range(0, len(kpn))]).astype(np.float32)
pts_f = np.array([kpf[i].pt for i in range(0, len(kpf))]).astype(np.float32)

print((np.square(pts_g - pts_n)).mean(axis=None))
print((np.square(pts_g - pts_f)).mean(axis=None))


# print(abs(np.linalg.norm(pts_g) - np.linalg.norm(pts_n)))
# print(abs(np.linalg.norm(pts_g) - np.linalg.norm(pts_f)))


# ground_kp = cv2.drawKeypoints(ground, kpg, None, color=(0,255,0), flags=cv2.DrawMatchesFlags_DEFAULT)

# near_kp = cv2.drawKeypoints(near, kpn, None, color=(0,255,0), flags=cv2.DrawMatchesFlags_DEFAULT)

# kpf = orb.detect(far)
# far_kp = cv2.drawKeypoints(far, kpn, None, color=(0,255,0), flags=cv2.DrawMatchesFlags_DEFAULT)


# plt.figure()
# plt.imshow(np.hstack([ground_kp, near_kp, far_kp]))
# plt.show()
# plt.close()