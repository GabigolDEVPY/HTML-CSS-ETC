from flask import Blueprint, abort, request, render_template, session


edit_bp = Blueprint('edit', __name__)


@edit_bp.route("/edit", methods=["GET", "PUT"])
def return_edit():
    if 'email' and 'senha' in session:
        if request.method == "GET":
            return render_template("edit.html")
        if request.method == "PUT":
            data = request.form.to_dict()
            return render_template("edit.html")
    else:
        abort(403)
        
@edit_bp.route('/return-product', methods=["GET"])
def return_product():
    product = ['1']
    product_id = request.args.get('id')
    # return render_template("edit.html", error="erro")             
    return render_template("edit.html", product=product)   


@edit_bp.route('/edit-product', methods=["POST"])
def edit_product():
    return render_template("edit.html")
