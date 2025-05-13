from flask import Blueprint, render_template, request, session, redirect, url_for, abort
from ..db.db_connect import get_connection

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
        
        # conexão com mysql
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        
        #selecionar o id do usuário
        try:
            cursor.execute("SELECT id FROM usuarios WHERE email = %s AND senha_hash = %s",(session['email'], session['senha']))
            id = cursor.fetchone()['id']
            
            # retornar itens mysql
            cursor.execute("SELECT id, descricao, nome, img_url, tipo FROM produtos WHERE usuario_id = %s",(id,))
            itens = cursor.fetchall()
            return render_template("home.html", itens=itens)
        
        except:
            return render_template("login.html", error="Erro ao fazer login")
            
    
    
    
    
    if request.method == "GET":
        if 'email' and 'senha' in session:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            
            cursor.execute("SELECT id FROM usuarios WHERE email = %s",(session['email'],))
            id = cursor.fetchone()['id']

            
            cursor.execute("SELECT id, descricao, nome, img_url, preco, tipo FROM produtos WHERE usuario_id = %s",(id,))
            itens = cursor.fetchall()

            return render_template("home.html", itens=itens)
        else:
            abort(403)