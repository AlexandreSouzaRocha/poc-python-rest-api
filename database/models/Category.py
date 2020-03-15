from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.db import db

class Category(db.Model):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'flask'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name