from flask import Flask, request
from predict_endpoint import img_bp
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_bad_request(e):
    print(e)
    return 'bad request!', 404

app.register_blueprint(img_bp, url_prefix="/predict")
app.register_error_handler(400, handle_bad_request)

'''
id: uuid
type: artifcat/monument
name: string
description: text
'''


if __name__ == "__main__":
    app.run(port=5000, debug=True)