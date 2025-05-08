from flask import Blueprint, render_template, request, session, abort
from ..db.dados import itens

add_bp = Blueprint("add", __name__)


@add_bp.route("/add", methods=["GET", "POST"])
def return_add():
    if 'email' and 'senha' in session:
        if request.method == "GET":
            return render_template("add.html")
        if request.method == "POST":
            data = request.form.to_dict()
            itens.append(data)
            return render_template("add.html")
    else:
        abort(403)      