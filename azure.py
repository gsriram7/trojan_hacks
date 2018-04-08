import requests

url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/describe"

headers = {
    'content-type': "application/octet-stream",
    'ocp-apim-subscription-key': "3b77f5936f004fadbf4bfe9b1c1a8574"
    }

def analyze_image(binary):
    response = requests.request("POST", url, headers=headers, data=binary)
    return response

# image_data = open('images/image1.png', 'rb').read()
# print('From azure.py: {}'.format(analyze_image(image_data).text))