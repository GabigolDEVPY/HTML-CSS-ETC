from flask import Blueprint

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/add', methods=["POST"])
def add():
    
    return "ok"