from flask import Blueprint, request
from ..controllers.controllers import user

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/add', methods=["POST"])
def add():
    data = request.get_json()
    user.create_user(data)
    return "ok"

@cliente_bp.route('/delete', methods=["GET"])
def delete():
    data = request.args.to_dict()
    user.delete_user(data)
    return "user deleted"

@cliente_bp.route('/update', methods=["PUT"])
def update():
    data = request.get_json()
    user.update_user(data)
    return "usuário atualizado"