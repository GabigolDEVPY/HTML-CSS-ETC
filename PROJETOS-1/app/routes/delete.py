from flask import Blueprint, abort, request, render_template, session
from ..db.db_connect import get_connection

delete_bp = Blueprint('delete', __name__)


@delete_bp.route("/delete", methods=["GET"])
def delete_product():
    dados = request.args.get('id')
    print(dados)
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM produtos WHERE id = %s",(dados,))
    connection.commit()
    return render_template("delete.html")
    
@delete_bp.route("/delete", methods=["GET"])
def return_delete():
    return render_template("delete.html")