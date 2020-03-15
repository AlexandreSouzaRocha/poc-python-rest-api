from marshmallow import Schema, pre_load, fields, validate
from database.db import ma

class CategorySchema(ma.Schema):

    id = fields.Integer()
    name = fields.String(required=True)

    def __init__(self, id, name):
        self.name = name
        self.id = id

        
        

