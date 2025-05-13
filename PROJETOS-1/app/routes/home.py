from flask import Blueprint, render_template, request, session, redirect, url_for, abort

home_bp = Blueprint('home', __name__)

@home_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login.return_login"))


@home_bp.route("/home", methods=["GET", "POST"])
def retornar_home():
    if request.method == "POST":
        data = request.form.to_dict()
        session['email'] = data['email']
        session['senha'] = data['senha']
        itens = ["1"]
        return render_template("home.html", itens=itens)
    if request.method == "GET":
        if 'email' and 'senha' in session:
            print(session)
            itens = ["1"]
            return render_template("home.html", itens=itens)
        else:
            abort(403)