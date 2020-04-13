import cv2
import zmq
import base64
import numpy as np
from model1 import model
model_ob = model()
context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://192.168.29.1:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        print(model_ob.predict(source))

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break
