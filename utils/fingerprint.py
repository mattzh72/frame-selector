import numpy as np
import cv2


def correlate(img, ground, size=(50, 50), corr=cv2.TM_SQDIFF_NORMED):
	# Convert to grayscale.
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ground = cv2.cvtColor(ground, cv2.COLOR_BGR2GRAY)

	# Resize everything down.
	ground_resize = cv2.resize(ground, size)
	img_resize = cv2.resize(img, size)

	# Get the correlation between the img and ground.
	return cv2.matchTemplate(img_resize, ground_resize, corr)[0][0]


def feature_MSE(img, ground, orb):
	# Convert to grayscale.
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ground = cv2.cvtColor(ground, cv2.COLOR_BGR2GRAY)

	# Find features and keypoints.
	kp_ground, kp_img = orb.detect(ground), orb.detect(img)
	pts_ground = np.array([kp_ground[i].pt for i in range(0, len(kp_ground))]).astype(np.float32)
	pts_img = np.array([kp_img[i].pt for i in range(0, len(kp_img))]).astype(np.float32)

	# Return MSE.
	return (np.square(pts_ground - pts_img)).mean(axis=None)

def feature_KNN(img, ground, orb):
	# Convert to grayscale.
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ground = cv2.cvtColor(ground, cv2.COLOR_BGR2GRAY)

	# Find features and keypoints.
	kp_ground, des_ground = orb.detectAndCompute(ground, None)
	kp_img, des_img = orb.detectAndCompute(img, None)

	# Brute force match.
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	matches = bf.knnMatch(des_ground, des_img, k=1)

	dist = np.array([m[0].distance for m in matches if m])

	# Return MSE.
	return np.square(dist).mean()





