from flask import Blueprint, render_template, request, session, abort
from ..db.db_connect import get_connection as gc

add_bp = Blueprint("add", __name__)


@add_bp.route("/add", methods=["GET", "POST"])
def return_add():
    if 'email' and 'senha' in session:
        if request.method == "GET":
            return render_template("add.html")
        
        elif request.method == "POST":
            data = request.form.to_dict()

            return render_template("add.html", mensagem="Produto cadastrado com sucesso")
    else:
        abort(403)      