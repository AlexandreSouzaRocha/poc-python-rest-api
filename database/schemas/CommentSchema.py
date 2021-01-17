from marshmallow import validate, pre_load, fields, Schema
from database.db import ma

class CommentSchema (ma.Schema):
    id = fields.Integer(dum_only=True)
    category_id = fields.Integer(required=True)
    comment = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
