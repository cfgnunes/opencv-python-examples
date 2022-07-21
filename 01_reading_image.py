"""
Example:
Read an image and display it.
"""

import cv2

image = cv2.imread("images/input.jpg")

cv2.imshow("Input image", image)

cv2.waitKey()
