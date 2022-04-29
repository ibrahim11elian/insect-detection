import json
import torch
import werkzeug
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
app = Flask(__name__)


# the path to saved wieghts
MODEL_PATH = 'best.pt'

# load model, first parameter is the path to the model folder
model = torch.hub.load('yolov5', 'custom',
                       path=MODEL_PATH, source='local', force_reload=True)
# model confedance
model.conf = 0.6

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

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
        # detection.save()

        # convert the data into json format
        preds_json_lst = json.loads(detection.pandas().xyxy[0].to_json(orient="records"))

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


if __name__ == '__main__':
   app.run()