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
    c = cv2.waitKey(10)
    if c == 27:
        break

cap.release()
