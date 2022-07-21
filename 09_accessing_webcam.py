"""
Example:
Show the video stream from a webcam.
"""

import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Input", frame)

    # Wait press ESC
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
