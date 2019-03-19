import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, img = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(
        gray, maxCorners=30, qualityLevel=0.05, minDistance=25)

    red_color = (0, 0, 255)

    for item in corners:
        x, y = item[0]
        cv2.circle(img, (x, y), 6, red_color, -1)

    cv2.imshow('Input', img)

    # Wait press ESC
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
