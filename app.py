from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from api.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alerts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True, port=5000)