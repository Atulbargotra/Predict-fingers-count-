from keras.models import load_model
import numpy as np
import cv2
class model:
    def __init__(self):
        self.classes = 'NONE ONE TWO THREE FOUR FIVE'.split()
        self.model = load_model('model_6cat.h5')
    def binaryMask(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (7,7), 3)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        ret, new = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return new


    def predict(self,image):
        x0, y0, width = 200,100, 300
        #frame = cv2.imread(image_link)
        #frame = image_link
        #dim = (300,300)
        # frame = cv2.resize(frame,dim)
        # get region of interest
        #roi = cropped = image.crop( ( x0, y0, x0 + width , y0 + width ) )
        roi = image[y0:y0+width,x0:x0+width]
        #open_cv_image = numpy.array(roi) 
        roi = self.binaryMask(roi)
        img = np.float32(roi)/255.
        img = np.expand_dims(img, axis=0)
        img = np.expand_dims(img, axis=-1) 
        pred = self.classes[np.argmax(self.model.predict(img)[0])]
        return (pred)
