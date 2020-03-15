from flask import Flask
from app import api_bp
from utils.constants import BASE_PATH
from database.db import db

def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:X4ndy@943@localhost:5432/postgres"

    
    app.register_blueprint(api_bp, url_prefix=BASE_PATH)

    db.init_app(app)

    from database.models import Category, Comment
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)