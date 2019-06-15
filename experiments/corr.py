import numpy as np
import cv2
from matplotlib import pyplot as plt


# Load images
ground = cv2.imread("./data/ground.jpg", 0)
near = cv2.imread("./data/near.jpg", 0)
far = cv2.imread("./data/far.jpg", 0)

# Resize everything down
SIZE = (50, 50)
ground_resize = cv2.resize(ground, SIZE)
near_resize = cv2.resize(near, SIZE)
far_resize = cv2.resize(far, SIZE)

res = cv2.matchTemplate(near_resize, ground_resize, cv2.TM_SQDIFF_NORMED)
print("close:" + str(res[0]))
print(res)
plt.imshow(res,cmap = 'gray')
# plt.imshow(far,cmap = 'gray')
plt.show()
plt.close()

res = cv2.matchTemplate(far_resize, ground_resize, cv2.TM_SQDIFF_NORMED)
print("different:" + str(res[0]))


