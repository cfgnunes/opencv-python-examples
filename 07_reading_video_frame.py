import cv2

cap = cv2.VideoCapture('videos/chaplin.mp4')

# Check if the video is opened correctly
if not cap.isOpened():
    raise IOError("Could not open video")

frames_to_read = 120
frame_list = []

for i in range(frames_to_read):
    ret, frame = cap.read()

    if ret:
        frame_list.append(frame)

cap.release()

# Show the 10th frame
cv2.imshow('Frame 10', frame_list[10])

cv2.waitKey()
