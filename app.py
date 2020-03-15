from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import CategoryResource
from resources.Comments import CommentResource
from resources.AsyncRequest import AsynchronousResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/category')
api.add_resource(CommentResource, '/comment')
api.add_resource(AsynchronousResource, '/users')