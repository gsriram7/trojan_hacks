import urllib
import cv2
import numpy as np
import time
from urllib import request
from PIL import Image
import azure

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://10.120.12.116:8080/shot.jpg'

count = 1
while True:

    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    raw = Image.fromarray(img, 'RGB')
    image_file_name = 'images/image{}.png'.format(count)
    raw.save(image_file_name)
    count += 1
    print('loop')

    response = azure.analyze_image(open(image_file_name, 'rb').read())

    print('Analyzed Image: {}'.format(response.text))

    # put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    time.sleep(4)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break