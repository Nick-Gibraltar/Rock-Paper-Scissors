import cv2
from keras.models import load_model
import numpy as np
import time

def get_prediction():

    model = load_model('/home/nick/Documents/AICore/Vision-Model/keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    gestures = ["Rock", "Paper", "Scissors", "None"]

    seconds_left = 10

    while seconds_left > 0:
        start_time = time.time()
        
        while time.time()-start_time<1: 

            ret, frame = cap.read()    
            cv2.imshow('frame name', frame)
            # Press q to close the window
            #print(max(prediction))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        seconds_left-=1
        print(seconds_left)

    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image
    #prediction = tf.tensor.numpy(model(data))
    prediction = model.predict(data, verbose=False)
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return(gestures[np.argmax(prediction[0])])

print(get_prediction())