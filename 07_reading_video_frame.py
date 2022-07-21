"""
Example:
Read a frame from a video.
"""

import cv2

cap = cv2.VideoCapture("videos/chaplin.mp4")

# Check if the video is opened correctly
if not cap.isOpened():
    raise IOError("Could not open video")

frames_to_read = 120
frames = []

for i in range(frames_to_read):
    ret, frame = cap.read()

    if ret:
        frames.append(frame)

cap.release()

# Show the 10th frame
cv2.imshow("Frame 10", frames[10])

cv2.waitKey()
