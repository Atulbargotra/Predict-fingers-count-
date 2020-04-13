import requests
import cv2
import numpy as np
cam = cv2.VideoCapture(0)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)

content_type = 'image/jpeg'
headers = {'content-type': content_type}
def sendtoserver(frame):
    r, image = cv2.imencode('.jpg', frame)
    response = requests.post("http://0.0.0.0:5000/", data=image.tostring(), headers=headers)
    return response 
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    sendtoserver(frame)
    cv2.imshow("output",frame)
    key = cv2.waitKey(10) & 0xff
    if key == ord('q'):
            break
