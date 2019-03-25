import cv2

img = cv2.imread("images/input.jpg")
cv2.imshow("Input", img)

img_gaussian = cv2.GaussianBlur(img, (17, 17), 0)
cv2.imshow("Gaussian filter", img_gaussian)

cv2.waitKey()
