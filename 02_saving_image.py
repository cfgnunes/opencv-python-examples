"""
Example:
Convert an image to a grayscale and save it.
"""

import cv2

gray_image = cv2.imread("images/input.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Grayscale image", gray_image)

cv2.imwrite("output.jpg", gray_image)

cv2.waitKey()
