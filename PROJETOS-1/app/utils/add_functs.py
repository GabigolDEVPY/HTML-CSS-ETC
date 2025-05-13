from ..db.db_connect import get_connection as gc
from flask import render_template

def addProduct():
    print("chegou aqui")
    connection = gc()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    dados_bd = cursor.fetchone()
    print(dados_bd)

    return render_template("add.html", mensagem="Produto cadastrado com sucesso")
    