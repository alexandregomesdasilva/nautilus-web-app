from flask import Blueprint, render_template
from db import get_db_connection

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # On récupère tous les fonds de la base
    cursor.execute("SELECT * FROM fonds")
    fonds = cursor.fetchall()

    # Pour chaque fonds, on calcule son rendement et sa NAV actuelle
    # C'est une boucle qui "enrichit" chaque fonds avec des données calculées
    for fond in fonds:

        # On récupère les performances de CE fonds, du plus ancien au plus récent
        cursor.execute("""
            SELECT nav FROM performances 
            WHERE fund_id = %s 
            ORDER BY date ASC
        """, (fond["id"],))
        perfs = cursor.fetchall()

        if perfs:
            nav_debut = perfs[0]["nav"]   # premier NAV (le plus ancien)
            nav_fin = perfs[-1]["nav"]    # dernier NAV (le plus récent), -1 = dernier élément en Python

            # Formule du rendement : ((fin - début) / début) * 100
            fond["rendement"] = round(((nav_fin - nav_debut) / nav_debut) * 100, 2)
            fond["nav_actuelle"] = nav_fin
        else:
            # Pas de données de performance pour ce fonds
            fond["rendement"] = 0
            fond["nav_actuelle"] = 0

    cursor.close()
    conn.close()

    # Calculs globaux pour les KPIs
    aum_total = sum(fond["aum"] for fond in fonds)
    rendement_moyen = round(sum(fond["rendement"] for fond in fonds) / len(fonds), 2)

    return render_template("dashboard.html",
        fonds=fonds,
        aum_total=aum_total,
        rendement_moyen=rendement_moyen
    )