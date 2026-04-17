import csv
import io
from flask import Blueprint, render_template, Response
from db import get_db_connection

fonds_bp = Blueprint("fonds", __name__)

@fonds_bp.route("/fonds")
def liste_fonds():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # On récupère tous les fonds disponibles en base
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

    # La table composition stocke uniquement les IDs et les poids.
    # Le JOIN avec actions permet de récupérer le nom, ticker et secteur
    # de chaque action contenue dans le fonds.
    cursor.execute("""
        SELECT actions.nom, actions.ticker, actions.secteur, composition.poids
        FROM composition
        JOIN actions ON composition.action_id = actions.id
        WHERE composition.fund_id = %s
    """, (id,))
    composition = cursor.fetchall()

    # On récupère l'historique des NAV de ce fonds, triées du plus ancien
    # au plus récent pour pouvoir les afficher chronologiquement (ex: graphique).
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

    # Même JOIN que dans detail_fonds, mais on récupère en plus
    # pays et prix — des colonnes utiles dans le CSV mais pas affichées sur la page de détail.
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
    # io.StringIO() crée un faux fichier en mémoire (pas sur le disque)
    # On écrit dedans comme un vrai fichier, mais tout reste dans la RAM
    output = io.StringIO()

    # DictWriter transforme nos dicos Python en lignes CSV
    # fieldnames définit les colonnes et leur ordre dans le fichier final
    # delimiter=';' utilise le point-virgule comme séparateur (standard Excel en France)
    writer = csv.DictWriter(output, fieldnames=["nom", "ticker", "secteur", "pays", "prix", "poids"], delimiter=';')

    # Écrit la première ligne d'en-tête : nom;ticker;secteur;pays;prix;poids
    writer.writeheader()

    # Parcourt chaque dico dans composition et écrit une ligne CSV par action
    writer.writerows(composition)

    # On retourne le CSV comme fichier téléchargeable
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename=fonds_{id}.csv"}
    )