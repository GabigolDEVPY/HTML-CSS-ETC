from flask import render_template, abort
from ..db.db_connect import get_connection

def registerUser(dados):
    print(dados)
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("""INSERT INTO usuarios (nome, email, chave_key, senha_hash)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (dados['nome'], dados['email'], dados['key'], dados['senha'],))
        connection.commit()
        return render_template("login.html")
    except:
        return render_template("register.html", error="Erro ao cadastrar" )
        