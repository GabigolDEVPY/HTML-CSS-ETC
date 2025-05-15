from flask import Blueprint, render_template, session

login_bp = Blueprint('login', __name__)

@login_bp.route("/", methods=["GET"])
def return_login():
    print(session)
    return render_template("login.html")