import base64
import cv2
import zmq

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://127.25.25.25:5555')

camera = cv2.VideoCapture(0)  # init the camera
count = 0
while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        if count==100:
            footage_socket.send(jpg_as_text)
        count+=1

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        breaks
