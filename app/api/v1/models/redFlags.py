from flask import  jsonify
from datetime import date
import uuid

redFlags_list = []
class redFlag(object):

    def __init__(self):
        self.redFlags_list=redFlags_list

    
    def create(self, redFlagtype, comment, createdBy, location):
            redFlag_details = {}
            redFlag_details['createdBy'] = createdBy
            redFlag_details['redflagtype'] = redFlagtype
            redFlag_details['location'] = location
            redFlag_details['status'] = 'pending'
            redFlag_details['comment'] = comment
            redFlag_details['createdOn'] = date.today()
            redFlag_details['id'] = len(redFlags_list)+1

            redFlags_list.append(redFlag_details)
            redFlags=len(self.redFlags_list)
            print(redFlags)
            newredFlag = self.redFlags_list[redFlags - 1]
            return jsonify({
           "status": 201,
           "message": "Created succesfully",
           "data": newredFlag
       })

    # method to GET all incidents
    def get_all(self):
        return jsonify({
            "redFlags" : self.redFlags_list
    })
    def getBy_Id(self, id):
        for item in redFlags_list:
            if item['redFlagtype'] == 'redflag' and item['id'] == int(id):
                print('welldone')
                return item
        return "no item found"