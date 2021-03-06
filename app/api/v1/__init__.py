from flask import Blueprint
from flask_restful import Resource, Api

from app.api.v1.views.views import redFlags, incidents

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(redFlags, '/redFlags')
api.add_resource(incidents, '/incidents')