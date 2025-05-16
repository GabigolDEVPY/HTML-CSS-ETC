from flask import Blueprint, request, make_response, jsonify
from ..controllers.controllers import user



cliente_bp = Blueprint('cliente', __name__)



@cliente_bp.route('/add', methods=["POST"])
def add():
    data = request.get_json()
    user.create_user(data)
    return "ok"



@cliente_bp.route('/delete', methods=["DELETE"])
def delete():
    data = request.args.to_dict()
    user.delete_user(data)
    return "user deleted"



@cliente_bp.route('/update', methods=["PUT"])
def update():
    data = request.get_json()
    user.update_user(data)
    return "user updated"



@cliente_bp.route("/list", methods=["GET"])
def list():
    dados = user.list_user()
    return make_response(jsonify(dados))