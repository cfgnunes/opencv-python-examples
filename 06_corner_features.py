"""
Example:
Detect corners in an image.
"""

import cv2

image = cv2.imread("images/blox.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Input image", image)

corners = cv2.goodFeaturesToTrack(
    image_gray, maxCorners=30, qualityLevel=0.05, minDistance=25)

red_color = (0, 0, 255)

for corner in corners:
    x, y = corner[0]
    cv2.circle(image, (x, y), 3, red_color, -1)

cv2.imshow("Top 'k' features", image)

cv2.waitKey()
