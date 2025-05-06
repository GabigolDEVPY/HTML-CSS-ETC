from flask import Blueprint, render_template, request

register_bp = Blueprint("register",__name__)

@register_bp.route("/register", methods=["GET"])
def return_register():
    return render_template("register.html")

@register_bp.route("/register", methods=["POST"])
def register_user():
    dados = request.form.to_dict()
    print(dados)
    return render_template("register.html", error="Erro ao cadastrar")
