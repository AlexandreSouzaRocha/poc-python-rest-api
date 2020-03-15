from marshmallow import validate, pre_load, fields, Schema
from database.db import ma

class CommentSchema (ma.Schema):
    id = fields.Integer(dum_only=True)
    category_id = fields.Integer(required=True)
    comment = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
    
    def __init__(self, id, category_id, comment, creation_date) :
        self.id = id
        self.category_id = category_id
        self.comment = comment 
        self.creation_date = creation_date

