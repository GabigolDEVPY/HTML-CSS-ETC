from flask import Blueprint, abort, request, render_template, session
from ..db.db_connect import get_connection


edit_bp = Blueprint('edit', __name__)


@edit_bp.route("/edit", methods=["GET", "PUT"])
def return_edit():
    if 'email' and 'senha' in session:
        if request.method == "GET":
            return render_template("edit.html")
    else:
        abort(403)
        
@edit_bp.route('/return-product', methods=["GET"])
def return_product():
    product_id = request.args.get('id')
    # conexao SQL
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, descricao, img_url, preco, tipo FROM produtos WHERE id = %s",(product_id,))
    product = cursor.fetchone()
    print(product)
    
    
    # return render_template("edit.html", error="erro")             
    return render_template("edit.html", product=product)   


@edit_bp.route('/edit-product', methods=["POST"])
def edit_product():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    dados = request.form.to_dict()
    print(dados)
    valores = (dados['nome'], dados['descricao'], dados['img_url'], dados['preco'], dados['tipo'], int(dados['id']))
    cursor.execute("UPDATE produtos SET nome = %s, descricao = %s, img_url = %s, preco = %s, tipo = %s WHERE id= %s", valores)
    connection.commit()
    return render_template("edit.html")
