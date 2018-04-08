import requests

url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/3046681e-d23b-4f09-bebe-a2e3d4390264/image"

headers = {
    'Content-Type': "application/octet-stream",
    'Prediction-Key': "fcba3104dc9a42daa360fa3123eea346"
    }

def analyze_image(binary):
    response = requests.request("POST", url, headers=headers, data=binary)
    return response.json()['Predictions']

# image_data = open('/Users/selvaram/Downloads/dhan.jpg', 'rb').read()
# response = analyze_image(image_data)
# print('From azure.py: {}'.format(response))