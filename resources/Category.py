from flask import request
from flask_restful import Resource
from database.models import Category, Comment
from database.db import db
from database.schemas.CategorySchema import CategorySchema

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class CategoryResource(Resource):
    
    def get(self):
        categories = Category.query.all()
        response_data = categories_schema.dump(categories).data
        return {
            'status': 'sucessful',
            'response': response_data
        }, 200
    
    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 400
        
        data, errors = category_schema.load(**json_data)

        if errors:
            return errors, 422
        
        category = Category.query.filter_by(name=data['name']).first()

        if category:
            return { 'message': 'The category ' + data['name'] + 'already exists' }, 409
        
        category = Category(
            name=data['name']
        )
        db.session.add(category)
        db.session.commit()

        response = category_schema.dump(category).data

        return {
            'status': 'sucessful',
            'response': response
        }, 201
    
    def put(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 400
        
        data, errors = category_schema.load(**json_data)

        if errors:
            return errors, 422
        
        category = Category.query.filter_by(id=data['id']).first()

        if not category:
            return { 'message': 'The category.id ' + data['id'] + 'don\'t exists' }, 404
        
        category = data['name']
        db.session.commit()

        response = category_schema.dump(category).data

        return {
            'status': 'sucessful',
            'response': response
        }, 200
    
    def delete(self):
        json_data = request.get_josn(force=True)

        if not json_data:
            return {
                'message': 'No input data provided'
            }, 400
        
        data, errors = category_schema.load(**json_data)

        if errors:
            return errors, 422
        
        category = Category.query.filter_by(id=data['id']).delete()
        db.session.commit()

        response = category_schema.dump(category).data

        return {
            'message': 'successful',
            'response': response
        }, 204