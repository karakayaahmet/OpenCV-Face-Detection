import cv2

cap = cv2.VideoCapture("faces.mp4")

face_cascade = cv2.CascadeClassifier("frontalfaces.xml")