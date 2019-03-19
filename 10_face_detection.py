import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Loads the classifier
face_cascade = cv2.CascadeClassifier(
    './cascade_files/haarcascade_frontalface_alt.xml')

while True:
    ret, frame = cap.read()

    # Detect faces
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=3)

    # Draw a rectangle in image
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
