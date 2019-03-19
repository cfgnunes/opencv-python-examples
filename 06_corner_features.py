import cv2

img = cv2.imread('images/blox.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Input image", img)

corners = cv2.goodFeaturesToTrack(
    gray, maxCorners=30, qualityLevel=0.05, minDistance=25)

red_color = (0, 0, 255)

for item in corners:
    x, y = item[0]
    cv2.circle(img, (x, y), 3, red_color, -1)

cv2.imshow("Top 'k' features", img)

cv2.waitKey()
