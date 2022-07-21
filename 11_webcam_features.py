"""
Example:
Detect corners from a webcam video stream.
"""

import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(
        frame_gray, maxCorners=30, qualityLevel=0.05, minDistance=25)

    red_color = (0, 0, 255)

    for corner in corners:
        x, y = int(corner[0][0]), int(corner[0][1])
        cv2.circle(frame, (x, y), 6, red_color, -1)

    cv2.imshow("Input", frame)

    # Wait press ESC
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
