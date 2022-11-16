import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('/home/nick/Documents/AICore/Vision-Model/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

start = time.time()
elapsed = 0
while elapsed < 3: 
    ret, frame = cap.read()
    '''

    '''
    cv2.imshow('frame', frame)
    '''# Press q to close the window
    print(prediction)
    '''
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
            
# After the loop release the cap object
resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
image_np = np.array(resized_frame)
normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
data[0] = normalized_image
prediction = model.predict(data)


cap.release()
# Destroy all the windows
cv2.destroyAllWindows()