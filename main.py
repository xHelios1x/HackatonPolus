import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import io, color, measure
#
# img = cv2.imread('images/grain (2).jpg', 0)
#
# if img is None:
#     sys.exit("Could not read the image.")
#
#
# cv2.imshow('lol', rgb)
# cv2.waitKey(0)

pixels_to_mm = 2

cap = cv2.VideoCapture('videos/fulltest.mp4')

while True:
    success, imgorig = cap.read()
    img = cv2.cvtColor(imgorig, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (11,11), 0)
    canny = cv2.Canny(blur, 2, 47, 3)

    dilated = cv2.dilate(canny, (1, 1), iterations = 3)

    (cnt, hierarchy) = cv2.findContours(dilated[550:,450:1150].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(imgorig, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb[550:,450:1150], cnt, -1, (0,0,255), 1)

    cv2.imshow('lol',rgb)
    #qcv2.waitKey(0)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# plt.hist(img.flat, bins=100, range=(0, 255))
# plt.show()
