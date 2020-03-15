from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from database.models import Category
from database.db import db

class Comment(db.Model):
    __tablename__ = 'comments'
    __table_args__ = {'schema': 'flask'}

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('flask.categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('comments', lazy='dynamic'))

    def __init__(self, comment, category_id):
        self.comment = comment
        self.category_id = category_id
    

