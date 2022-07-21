"""
Example:
Apply a Gaussian filter in an image.
"""

import cv2

image = cv2.imread("images/input.jpg")
cv2.imshow("Input", image)

image_gaussian = cv2.GaussianBlur(image, (17, 17), 0)
cv2.imshow("Gaussian filter", image_gaussian)

cv2.waitKey()
