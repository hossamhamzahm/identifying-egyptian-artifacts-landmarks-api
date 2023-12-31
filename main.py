from flask import Flask
from flask_cors import CORS
from router.predict_endpoint import img_bp
from router.cls_endpoint import clses_bp
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
CORS(app)


@app.errorhandler(HTTPException)
def handle_bad_request(e):
    print(e)
    error_object = {
        "error": e.name, #"404, Page not found!",
        "message": e.description, #"Visit /classes",
        "code": e.code
    }
    return error_object, 404



app.register_blueprint(img_bp, url_prefix="/predict")
app.register_blueprint(clses_bp, url_prefix="/classes")
app.register_error_handler(400, handle_bad_request)


port = os.getenv('PORT') if os.getenv('PORT') else 5000

if __name__ == "__main__":
    app.run(port=port, debug=True)