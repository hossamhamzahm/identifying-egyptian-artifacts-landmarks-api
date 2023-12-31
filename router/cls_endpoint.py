from flask import Blueprint, request
from handler.Artifact import find_by_name, find_by_cnn_id, find_by_id, find_all


clses_bp = Blueprint("classes", __name__)


@clses_bp.route("/", methods=["GET"])
def index():
    payload = {
        'results': []
    }

    args = request.args
    clses = {}

    if args.get("q"): 
        q = args.get("q")
        clses = find_by_name(q)
    elif args.get("cnn_id"): 
        cnn_id = args.get("cnn_id")
        clses = find_by_cnn_id(cnn_id)
    else:
        clses = find_all()

    for cls in clses:
        cls = cls.__dict__
        del cls['_sa_instance_state']
        payload['results'].append(cls)

    return payload, 200



@clses_bp.route("/<string:id>", methods=["GET"])
def show_class(id):
    payload = {
        'results': []
    }

    cls = find_by_id(id).__dict__
    del cls['_sa_instance_state']
    payload['results'].append(cls)

    return payload, 200