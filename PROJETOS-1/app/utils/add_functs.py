from ..db.db_connect import get_connection as gc
from flask import render_template

def addProduct(data, email):
    data = data
    email = email
    print(email)
    connection = gc()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    dados_bd = cursor.fetchone()

    return render_template("add.html", mensagem="Produto cadastrado com sucesso")
    