from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import store

app = Flask(__name__)
CORS(app)

cameras_to_ip = {'camera1': 'http://10.120.12.116:8080'}

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/find", methods=["POST"])
def find():
    item = request.form['item']
    print(item)
    response = store.get(item)
    response['ip'] = '{}/browserfs.html'.format(cameras_to_ip[response['camera']])
    print(response['camera'])
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')