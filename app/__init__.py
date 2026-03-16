from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret123"
    app.config["MONGO_URI"] = "mongodb://localhost:27017/finance_tracker"

    mongo.init_app(app)

    from app.routes.auth import auth
    from app.routes.transaction import transaction
    from app.routes.dashboard import dashboard

    app.register_blueprint(auth)
    app.register_blueprint(transaction)
    app.register_blueprint(dashboard)

    return app