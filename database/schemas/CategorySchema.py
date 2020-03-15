from marshmallow import Schema, pre_load, fields, validate
from database.db import ma

class CategorySchema(ma.Schema):

    id = fields.Integer()
    name = fields.String(required=True)

        
        

