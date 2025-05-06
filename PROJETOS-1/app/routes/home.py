from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)



users = [
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289},
    {"name": "Gabriel", "key": 1231231, "points": 3322, "number": 998473289}
]




@home_bp.route("/home", methods=["GET", "POST"])
def retornar_home():
    return render_template("home.html", users=users)