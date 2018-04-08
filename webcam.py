import datetime
import cv2
import base64
import numpy as np
import time
from urllib import request
from PIL import Image
import azure
import store

cameras_to_ip = {'camera1': 'http://10.120.12.116:8080'}

list_of_cameras = cameras_to_ip.keys()

count = 1


def construct_update_dict(predictions, camera, image_file_name):
    timestamp = datetime.datetime.now()
    result = {}
    result['camera'] = camera
    result['timestamp'] = timestamp
    with open(image_file_name, "rb") as image_file:
        result['image'] = str(base64.b64encode(image_file.read()))

    values = []
    for prediction in predictions:
        value = {}
        value['Tag'] = prediction['Tag']
        value['Probability'] = prediction['Probability']
        values.append(value)
    result['values'] = values
    return result


while True:

    for camera in list_of_cameras:
        # Use urllib to get the image and convert into a cv2 usable format
        imgResp=request.urlopen('{}/shot.jpg'.format(cameras_to_ip[camera]))
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        raw = Image.fromarray(img, 'RGB')
        image_file_name = 'images/image{}.png'.format(count)
        raw.save(image_file_name)
        count += 1
        count = count % 9
        print('loop')

        response = azure.analyze_image(open(image_file_name, 'rb').read())

        put_dict = construct_update_dict(response, camera, image_file_name)

        store.put(put_dict)

        # put the image on screen
        cv2.imshow('IPWebcam',img)

        #To give the processor some less stress
        time.sleep(7)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break