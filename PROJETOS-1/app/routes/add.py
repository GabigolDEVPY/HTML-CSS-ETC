from flask import Blueprint, render_template, request, session, abort
from ..utils.add_functs import addProduct

add_bp = Blueprint("add", __name__)


@add_bp.route("/add", methods=["GET", "POST"])
def return_add():
    if 'email' and 'senha' in session:
        if request.method == "GET":
            return render_template("add.html")
        
        if request.method == "POST":
            data = request.form.to_dict()
            return addProduct(data, email=session['email'])
    else:
        abort(403)      