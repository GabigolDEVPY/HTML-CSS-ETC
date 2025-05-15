from ..db.db_connect import get_connection as gc
from flask import render_template, abort

def addProduct(data, email):
    data = data
    email = email
    connection = gc()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
    id_bd = cursor.fetchone()

    if id_bd:
        url = "fsdfjsdkjfkjsdfkds"
        cursor.execute("""INSERT INTO produtos ( usuario_id, nome, descricao, img_url, tipo, url_reference)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (int(id_bd['id']), data["name"], data["description"], data["url"], data["type"], url))
        connection.commit()

        return render_template("add.html", mensagem="Produto cadastrado com sucesso")
    
    else:
        abort(403)