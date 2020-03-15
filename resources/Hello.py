from flask_restful import Resource

class Hello(Resource):

    def get (self):
        return {
            "message": "GET from Flask!"
        }
    
    def post (self):
        return {
            "message": "POST from Flask"
        }