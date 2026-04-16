import csv
import io
from flask import Blueprint, render_template, Response
from db import get_db_connection

fonds_bp = Blueprint("fonds", __name__)

@fonds_bp.route("/fonds")
def liste_fonds():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM fonds")
    fonds = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("fonds.html", fonds=fonds)

@fonds_bp.route("/fonds/<int:id>")
def detail_fonds(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Les infos du fonds
    cursor.execute("SELECT * FROM fonds WHERE id = %s", (id,))
    fond = cursor.fetchone()  # fetchone() car on veut UN seul résultat

    # La composition avec un JOIN
    cursor.execute("""
        SELECT actions.nom, actions.ticker, actions.secteur, composition.poids
        FROM composition
        JOIN actions ON composition.action_id = actions.id
        WHERE composition.fund_id = %s
    """, (id,))
    composition = cursor.fetchall()

    # Les performances
    cursor.execute("""
        SELECT date, nav FROM performances
        WHERE fund_id = %s
        ORDER BY date ASC
    """, (id,))
    performances = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("detail_fonds.html",
        fond=fond,
        composition=composition,
        performances=performances
    )

@fonds_bp.route("/fonds/<int:id>/export")
def export_fonds(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # On récupère la composition du fonds
    cursor.execute("""
        SELECT actions.nom, actions.ticker, actions.secteur, 
               actions.pays, actions.prix, composition.poids
        FROM composition
        JOIN actions ON composition.action_id = actions.id
        WHERE composition.fund_id = %s
    """, (id,))
    composition = cursor.fetchall()

    cursor.close()
    conn.close()

    # On crée le CSV en mémoire
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["nom", "ticker", "secteur", "pays", "prix", "poids"], delimiter=';')
    writer.writeheader()
    writer.writerows(composition)

    # On retourne le CSV comme fichier téléchargeable
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename=fonds_{id}.csv"}
    )