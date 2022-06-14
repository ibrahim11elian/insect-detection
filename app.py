import json
import torch
import numpy as np
import werkzeug
from PIL import Image
import cv2
import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
app = Flask(__name__)


# the path to saved wieghts
MODEL_PATH = 'best.pt'

# load model, first parameter is the path to the model folder
model = torch.hub.load('yolov5', 'custom',
                       path=MODEL_PATH, source='local', force_reload=True)
# model confedance
model.conf = 0.7


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def home():
    # number of mediterranean fruit fly insects
    cc_counter = 0

    # number peach fruit fly insects
    bz_counter = 0

    # list of detected insects
    results = []

    if (request.method == 'POST'):
        imagefile = request.files['image']

        # extract the image name from image
        filename = werkzeug.utils.secure_filename(imagefile.filename)

        # save the image to the data folder
        imagefile.save("./Data/" + filename)

        img = Image.open("./Data/" + filename)
        new_image = img.resize((640, 640))
        imge = np.array(new_image)
        gray = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

        # run inference
        detection = model([gray], size=1280)

        # convert the data into json format
        preds_json_lst = json.loads(
            detection.pandas().xyxy[0].to_json(orient="records"))

        for preds_json in preds_json_lst:
            results.append({
                "DETECTION_TYPE": preds_json['name'],
                "COORDINATES": {'xmin': int(preds_json['xmin']),
                                'ymin': int(preds_json['ymin']),
                                'xmax': int(preds_json['xmax']),
                                'ymax': int(preds_json['ymax']),
                                },
                "SCORE": preds_json['confidence']
            })
            if preds_json['name'] == 'CC':
                cc_counter += 1
            else:
                bz_counter += 1
        return jsonify({
            'cod': 200,
            'n_cc': f"{cc_counter}",
            'n_bz': f"{bz_counter}",
            'results': results,
            "message": "Image Uploaded Successfully"
        })
    else:
        return jsonify({
            'cod': 404,
            "message": "Image Uploade Faild"
        })


@app.route('/detect/web', methods=['POST'])
def detect():
    # number of mediterranean fruit fly insects
    cc_counter = 0

    # number peach fruit fly insects
    bz_counter = 0

    # list of detected insects
    results = []

    if (request.method == 'POST'):

        # take the image url to dowenload
        image_url = request.args.get('image')

        # extract the file name from the url
        filename = image_url.split('/')[-1]

        r = requests.get(image_url, allow_redirects=True)

        image_path = "./Data/image.jpg"

        open(image_path, 'wb').write(r.content)
        img = Image.open(image_path)
        new_image = img.resize((640, 640))
        imge = np.array(new_image)
        gray = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

        # run inference
        detection = model([gray], size=1280)

        # convert the data into json format
        preds_json_lst = json.loads(
            detection.pandas().xyxy[0].to_json(orient="records"))

        for preds_json in preds_json_lst:
            results.append({
                "DETECTION_TYPE": preds_json['name'],
                "COORDINATES": {'xmin': int(preds_json['xmin']),
                                'ymin': int(preds_json['ymin']),
                                'xmax': int(preds_json['xmax']),
                                'ymax': int(preds_json['ymax']),
                                },
                "SCORE": preds_json['confidence']
            })
            if preds_json['name'] == 'CC':
                cc_counter += 1
            else:
                bz_counter += 1
        return jsonify({
            'cod': 200,
            'n_cc': f"{cc_counter}",  # cc count
            'n_bz': f"{bz_counter}",  # bz count
            'results': results,
            "message": "Image Uploaded Successfully"
        })
    else:
        return jsonify({
            'cod': 404,
            "message": "Image Uploade Faild"
        })


if __name__ == '__main__':
    app.run()
