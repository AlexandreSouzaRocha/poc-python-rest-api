from flask import jsonify, request
from flask_restful import Resource
from database.models.Comment import Comment
from database.models.Category import Category
from database.schemas.CommentSchema import CommentSchema
from database.db import db

comments_schema = CommentSchema()
comment_schema = CommentSchema(many=True)

class CommentResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema.dump(comments).data

        return {
            'status': 'successful',
            'response': comments
        }, 200
    
    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return { 'message': 'No input data provided' }, 400
        
        data, errors = comment_schema.load(**json_data)

        if errors:
            return {'status': 'error', 'response': errors }, 422
        
        category_id = Category.query.filter_by(id=data['category_id']).first()

        if not category_id:
            return {
                'status': 'error',
                'message': 'Category doesn\'t exists or not found'
            }, 404