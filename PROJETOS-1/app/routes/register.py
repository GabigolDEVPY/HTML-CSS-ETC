from flask import Blueprint, render_template, request
from ..utils.register_user import registerUser

register_bp = Blueprint("register",__name__)


# retornar tela de registro
@register_bp.route("/register", methods=["GET"])
def return_register():
    return render_template("register.html")


# cadastrar usuário
@register_bp.route("/register", methods=["POST"])
def register_user():
    dados = request.form.to_dict()
    return registerUser(dados)
