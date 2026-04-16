from flask import Flask
from routes.fonds import fonds_bp
from routes.actions import actions_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(fonds_bp)
app.register_blueprint(actions_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)