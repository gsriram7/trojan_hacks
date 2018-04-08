import json, base64, datetime


classes = set(['keys', 'mobile', 'dhanshri', 'idcard'])


def get_db():
    with open("db.json", 'r') as fp:
        db = dict(json.load(fp))
    fp.close()
    return db.copy()


def get(item):
    db_copy = get_db()
    cameras = db_copy.keys()
    result = {}
    result['item'] = item
    result['max'] = {}

    max_camera = 0
    max_confidence = -100.0
    for camera in cameras:
        if db_copy[camera][item]['max']['confidence'] > max_confidence:
            max_camera = camera
            max_confidence = db_copy[camera][item]['max']['confidence']

    result['camera'] = max_camera
    result['max'] = db_copy[max_camera][item]['max']

    return result


def put(item):
    camera = item['camera']
    image = item['image']
    timestamp = item['timestamp']
    db_copy = get_db()

    for value in item['values']:
        tag = value['Tag']
        confidence = value['Probability']

        if tag in classes and db_copy[camera][tag]['max']['confidence'] < confidence:
            db_copy[camera][tag]['max']['confidence'] = confidence
            db_copy[camera][tag]['max']['image'] = image
            db_copy[camera][tag]['max']['timestamp'] = str(timestamp)

    with open('db.json', 'w', encoding='utf8') as fp:
        json.dump(db_copy, fp, indent=4, ensure_ascii=False)
    fp.close()


up = {'camera': 'camera2',
      'image': 'images/image1.png',
      'timestamp': str(datetime.datetime.now()),
      'values': [
          {
            "Tag": "keys",
            "Probability": 0.99
          },
          {
              "Tag": "phone",
              "Probability": 0.3605307
          },
          {
              "Tag": "dhanshri",
              "Probability": 0.99
          }
      ]}

# print(get('dhanshri'))