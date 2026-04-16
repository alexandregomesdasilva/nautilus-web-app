from flask import Blueprint, render_template
from db import get_db_connection

actions_bp = Blueprint("actions", __name__)

@actions_bp.route("/actions")
def liste_actions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # On récupère toutes les actions disponibles en base
    cursor.execute("SELECT * FROM actions")
    actions = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("actions.html", actions=actions)