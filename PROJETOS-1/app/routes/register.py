from flask import Blueprint, render_template

register_bp = Blueprint("register",__name__)

@register_bp.route("/register", methods=["GET"])
def return_register():
    return render_template("register.html")
