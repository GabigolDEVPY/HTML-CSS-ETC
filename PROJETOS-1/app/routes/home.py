from flask import Blueprint, render_template, request, session, redirect, url_for, abort

home_bp = Blueprint('home', __name__)

itens = [
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312},
    {"name": "Telefone", "description": "231fasdfsdaafsadfsd231", "url": "https://mkt.multilaser.com.br/emkt/mkt/resizer/2022/laminas-html/office/TC065/assets/img/tc193_00.jpg", "type": "casa", "price": 12312}
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
        return render_template("home.html", itens=itens)
    if request.method == "GET":
        if 'email' and 'senha' in session:
            print(session)
            return render_template("home.html", itens=itens)
        else:
            abort(403)