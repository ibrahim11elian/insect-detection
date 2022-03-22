import json
import torch
import flask
from flask import request, jsonify
import werkzeug
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# the path to saved wieghts
MODEL_PATH = 'best.pt'

# load model, first parameter is the path to the model folder
model = torch.hub.load('yolov5', 'yolov5m',
                       force_reload=True)
# model confedance
model.conf = 0.6


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

        # run inference
        detection = model(["./Data/" + filename], size=1280)

        # display results
        detection.save()

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


# app.run()
