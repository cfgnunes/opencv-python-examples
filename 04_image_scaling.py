import cv2

img = cv2.imread("images/input.jpg")

img_scaled = cv2.resize(img, (200, 200))

cv2.imshow("Scaling - Skewed Size", img_scaled)

cv2.waitKey()
