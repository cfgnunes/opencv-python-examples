"""
Example:
Play a video.
"""

import cv2

cap = cv2.VideoCapture("videos/chaplin.mp4")

# Check if the video is opened correctly
if not cap.isOpened():
    raise IOError("Could not open video")

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Input", frame)

    # Wait press ESC
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
