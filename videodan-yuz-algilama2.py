import cv2

cap = cv2.VideoCapture("faces.mp4")

face_cascade = cv2.CascadeClassifier("frontalfaces.xml")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)