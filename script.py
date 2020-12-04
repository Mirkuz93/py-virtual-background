import cv2
import requests
import numpy as np

def get_mask(frame, bodypix_url='http://localhost:8080/mask'):

    _, data = cv2.imencode(".jpg", frame)

    r = requests.post(
        url=bodypix_url,
        data=data.tobytes(),
        headers={'Content-Type': 'application/octet-stream'})
    print(r)

    # convert raw bytes to a numpy array

    # raw data is uint8[width * height] with value 0 or 1
    mask = np.frombuffer(r.content, dtype=np.uint8)
    mask = mask.reshape((frame.shape[0], frame.shape[1]))
    return mask

cap = cv2.VideoCapture('/dev/video0')

height, width = 720, 1280

cap.set(cv2.CAP_PROP_FRAME_WIDTH ,width)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

cap.set(cv2.CAP_PROP_FPS, 60)

success, frame = cap.read()

cv2.imwrite("test.jpg", frame)
get_mask(frame)

