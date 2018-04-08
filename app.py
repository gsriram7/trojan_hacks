from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route("/find", methods=["GET"])
def find():
    item = request.args.get('item')
    return jsonify({'item': item})


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')