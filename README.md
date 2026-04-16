# Nautilus 🌊

Application web de visualisation et d'analyse de portefeuilles d'actions.

## Stack technique

- **Backend** : Python / Flask
- **Base de données** : MySQL (MariaDB)
- **Frontend** : HTML / Tailwind CSS / JavaScript / Chart.js
- **Templating** : Jinja2

## Prérequis

- Python 3.10+
- MySQL ou MariaDB (XAMPP recommandé)
- Git

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/AlexandreGomesDaSilva/nautilus-app.git
cd nautilus-app
```

### 2. Créer et activer l'environnement virtuel

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install flask mysql-connector-python
```

### 4. Créer la base de données

Démarre MySQL (via XAMPP ou autre), puis importe le script de création :

```bash
mysql -u root -p < database.sql
```

Ou exécute le contenu de `database.sql` directement dans phpMyAdmin.

### 5. Configurer la connexion

Dans `db.py`, vérifie les paramètres de connexion :

```python
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",       # ton mot de passe si nécessaire
    database="nautilus"
)
```

### 6. Lancer l'application

```bash
python app.py
```

L'application est accessible sur **http://127.0.0.1:5000**

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Dashboard — vue d'ensemble des fonds avec KPIs |
| `/fonds` | Liste de tous les fonds |
| `/fonds/<id>` | Détail d'un fonds — composition et performances |
| `/fonds/<id>/export` | Export CSV de la composition d'un fonds |
| `/actions` | Catalogue des actions |

---

## Structure du projet

```
nautilus-app/
├── app.py              # Point d'entrée, enregistrement des blueprints
├── db.py               # Connexion MySQL
├── database.sql        # Script de création et données de test
├── routes/
│   ├── dashboard.py    # Route page d'accueil
│   ├── fonds.py        # Routes liste et détail des fonds
│   └── actions.py      # Route liste des actions
└── templates/
    ├── base.html        # Layout commun (navbar, Tailwind)
    ├── dashboard.html   # Dashboard avec KPIs
    ├── fonds.html       # Liste des fonds
    ├── detail_fonds.html # Détail + graphique NAV
    └── actions.html     # Liste des actions
```

---

## Fonctionnalités

- **Dashboard** — KPIs globaux (nombre de fonds, AUM total, rendement moyen) et tableau récapitulatif
- **Liste des Fonds** — Consultation de tous les fonds avec informations clés
- **Détail d'un Fonds** — Composition détaillée, répartition sectorielle et graphique de performances NAV
- **Liste des Actions** — Catalogue complet avec ticker, secteur et pays
- **Export CSV** — Export de la composition d'un fonds en un clic
