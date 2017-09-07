##
 #
 # Created by Rambod Rahmani.
 # Section 4 - Image Theory
 # access_pixels.py
 #
 ##

import cv2
import numpy as np

img = cv2.imread("me.jpg")

print(img[1][1])

img[1][1][0] = 255
img[1][1][1] = 255
img[1][1][2] = 255

py = 100
px = 100

img[px][py][0] = 255
img[px][py][1] = 255
img[px][py][2] = 255

cv2.imshow("Rambod Rahmani Picture", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
