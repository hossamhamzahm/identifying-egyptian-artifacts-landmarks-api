from flask import Blueprint, request, redirect
import os
from CNN.model import predict


img_bp = Blueprint("img", __name__)


@img_bp.route("/", methods=["POST"])
def upload_image():
    if request.files:
        image = request.files["image"]
        file_name =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploaded_imgs", image.filename)

        # save the image in uploaded_imgs directory
        image.save(file_name)

        # predice image class
        class_name = predict(file_name)

        # remove the image
        os.remove(file_name)

        payload = {
            "id": "cff6d5f3-f56e-409a-a84b-c2601763caee",
            "name": class_name, 
            "type": "artifcat/monument",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        }

        return payload, 200
    
    error_object = {
        "error":"Missing request body",
        "message":"Request body has no image",
        "details":"/api/book/1"
    }
    return error_object, 400



