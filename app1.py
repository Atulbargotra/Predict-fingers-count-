from flask import Flask, url_for, send_from_directory, request
from model1 import model
model_ob = model()
import numpy as np
import cv2
app = Flask(__name__)
@app.route("/", methods=["POST"])
def home():
    r = request
    nparr = np.fromstring(r.data,np.uint8)
    img=cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    resp = model_ob.predict(img)
    print(resp)
    return resp

if __name__ == '__main__':
    app.run(host='192.168.29.37', debug=False,threaded=False)
