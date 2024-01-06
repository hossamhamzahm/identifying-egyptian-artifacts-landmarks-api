from flask import Blueprint, request, redirect
import os
from CNN.model import predict as resnet
from SNN.model import predict as snn
from handler.Artifact import find_by_name, find_by_cnn_id


img_bp = Blueprint("img", __name__)


@img_bp.route("/", methods=["POST"])
def upload_image():
    if request.files:
        image = request.files["image"]
        file_name =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "uploaded_imgs", image.filename)

        # save the image in uploaded_imgs directory
        image.save(file_name)

        # predict image class
        prediction_data = resnet(file_name)

        # remove the image
        os.remove(file_name)

        payload = {
            'results': []
        }

        cls = find_by_cnn_id(prediction_data['cnn_id']).__dict__
        del cls['_sa_instance_state']
        cls['accuracy'] = prediction_data['accuracy']
        payload['results'].append(cls)

        return payload, 200
    
    error_object = {
        "error":"Missing request body",
        "message":"Request body has no image",
        "code": 400
    }
    return error_object, 400



