from flask import Blueprint, render_template, request, session, redirect, url_for, abort

home_bp = Blueprint('home', __name__)

users = [
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289}
]

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
        return render_template("home.html", users=users)
    if request.method == "GET":
        if 'email' and 'senha' in session:
            print(session)
            return render_template("home.html", users=users)
        else:
            abort(404)