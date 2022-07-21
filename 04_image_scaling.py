"""
Example:
Scale an image.
"""

import cv2

image = cv2.imread("images/input.jpg")

image_scaled = cv2.resize(image, (200, 200))

cv2.imshow("Scaling - Skewed Size", image_scaled)

cv2.waitKey()
