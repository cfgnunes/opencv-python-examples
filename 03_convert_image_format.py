"""
Example:
Convert an image to another format and save it.
"""

import cv2

image = cv2.imread("images/input.jpg")

cv2.imwrite("output.png", image, [cv2.IMWRITE_PNG_COMPRESSION])
