from flask import jsonify, request, make_response
from flask_restful import Resource
from app.api.v1.models.redFlags import redFlag as redFlagMod

class redFlags(Resource):
    def __init__(self):
        self.redFlagObject = redFlagMod()
        def post(self):
            redFlags_data = request.get_json()
            redFlagtype = redFlags_data['redFlagtype']
            comment = redFlags_data['comment']
            createdBy = redFlags_data['createdBy']
            location = redFlags_data['location']
            
            response = self.redFlagObject.create(redFlagtype, comment, createdBy, location)
            return response

        def get(self):
            response = self.redFlagObject.get_all()
            return response
            
class incidents(Resource):
    def __init__(self):
        self.redFlagObject = redFlagMod 

    def get(self, id):
        response = self.redFlagObject.getBy_Id(self, id)
        return make_response(jsonify(response))