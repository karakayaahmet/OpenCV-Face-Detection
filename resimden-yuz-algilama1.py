import cv2

img = cv2.imread("face.png")

face_cascade = cv2.CascadeClassifier("frontalface.xml")